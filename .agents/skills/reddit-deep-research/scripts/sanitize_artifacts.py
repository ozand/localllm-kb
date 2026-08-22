#!/usr/bin/env python3
"""Audit and sanitize research text without modifying the input in place."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Iterable, TextIO

SCHEMA_VERSION = 1
PATTERNS = (
    ("windows-path", re.compile(r"(?<![A-Za-z0-9])(?:[A-Za-z]:[\\/]|\\\\)[^\s\"'<>]+"), "<windows-path>"),
    ("unix-path", re.compile(r"(?<!:)\/(?:home|Users|tmp|var|opt|srv|mnt)\/[^\s\"'<>]+"), "<unix-path>"),
    ("private-endpoint", re.compile(r"\b(?:(?:10|127)\.\d{1,3}\.\d{1,3}\.\d{1,3}|192\.168\.\d{1,3}\.\d{1,3}|172\.(?:1[6-9]|2\d|3[0-1])\.\d{1,3}\.\d{1,3})(?::\d{1,5})?\b"), "<private-endpoint>"),
    ("api-key", re.compile(r"(?i)(?:api[_-]?key|access[_-]?token|refresh[_-]?token|password)\s*[:=]\s*[^\s,;]+"), "<secret-assignment>"),
    ("bearer-token", re.compile(r"(?i)bearer\s+[A-Za-z0-9._~+\-/]+=*"), "Bearer <redacted>"),
    ("openai-key", re.compile(r"\bsk-[A-Za-z0-9_-]{8,}\b"), "<secret-key>"),
)


def sanitize_text(text: str) -> tuple[str, dict[str, int]]:
    counts = {name: 0 for name, _, _ in PATTERNS}
    result = text
    for name, pattern, replacement in PATTERNS:
        result, count = pattern.subn(replacement, result)
        counts[name] = count
    return result, {name: count for name, count in counts.items() if count}


def iter_files(input_path: Path) -> Iterable[Path]:
    if input_path.is_file():
        yield input_path
    elif input_path.is_dir():
        yield from sorted(path for path in input_path.rglob("*") if path.is_file())
    else:
        raise FileNotFoundError(input_path)


def audit_path(input_path: Path) -> dict:
    files = []
    total_counts: dict[str, int] = {}
    for path in iter_files(input_path):
        text = path.read_text(encoding="utf-8", errors="replace")
        _, counts = sanitize_text(text)
        for name, count in counts.items():
            total_counts[name] = total_counts.get(name, 0) + count
        relative = path.relative_to(input_path) if input_path.is_dir() else Path(path.name)
        files.append({"path": relative.as_posix(), "categories": counts, "matched": sum(counts.values())})
    return {
        "schema_version": SCHEMA_VERSION,
        "mode": "audit",
        "input": "<input>",
        "file_count": len(files),
        "matched_file_count": sum(item["matched"] > 0 for item in files),
        "category_counts": total_counts,
        "files": files,
    }


def sanitize_path(input_path: Path, output_path: Path) -> dict:
    if input_path.resolve() == output_path.resolve():
        raise ValueError("input and output must be different; source artifacts are immutable")
    if input_path.is_file():
        output_path.parent.mkdir(parents=True, exist_ok=True)
        sanitized, counts = sanitize_text(input_path.read_text(encoding="utf-8", errors="replace"))
        output_path.write_text(sanitized, encoding="utf-8", newline="\n")
        return {"schema_version": SCHEMA_VERSION, "mode": "sanitize", "input": "<input>", "output": "<output>", "file_count": 1, "category_counts": counts}
    if not input_path.is_dir():
        raise FileNotFoundError(input_path)
    files = []
    total_counts: dict[str, int] = {}
    for source in iter_files(input_path):
        relative = source.relative_to(input_path)
        target = output_path / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        sanitized, counts = sanitize_text(source.read_text(encoding="utf-8", errors="replace"))
        target.write_text(sanitized, encoding="utf-8", newline="\n")
        for name, count in counts.items():
            total_counts[name] = total_counts.get(name, 0) + count
        files.append({"input": relative.as_posix(), "output": relative.as_posix(), "categories": counts, "matched": sum(counts.values())})
    return {"schema_version": SCHEMA_VERSION, "mode": "sanitize", "input": "<input>", "output": "<output>", "file_count": len(files), "category_counts": total_counts, "files": files}


def emit(data: dict, stream: TextIO = sys.stdout) -> None:
    json.dump(data, stream, ensure_ascii=False, indent=2)
    stream.write("\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="mode", required=True)
    audit = subparsers.add_parser("audit", help="Report categories and counts without exposing matches.")
    audit.add_argument("--input", required=True, type=Path)
    sanitize = subparsers.add_parser("sanitize", help="Write a sanitized copy; never modifies input in place.")
    sanitize.add_argument("--input", required=True, type=Path)
    sanitize.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    try:
        result = audit_path(args.input) if args.mode == "audit" else sanitize_path(args.input, args.output)
        emit(result)
        return 0
    except (FileNotFoundError, ValueError, OSError) as exc:
        emit({"schema_version": SCHEMA_VERSION, "error": type(exc).__name__, "message": str(exc)}, sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
