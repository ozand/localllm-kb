#!/usr/bin/env python3
"""Render an auditable Reddit research run as OKF Markdown without inventing facts."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
from typing import Any


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def dump_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(text.rstrip() + "\n", encoding="utf-8")
    temporary.replace(path)


def kebab(value: str) -> str:
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", value.lower())).strip("-")


def yaml_quote(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def render_corpus(run_dir: Path, run: dict[str, Any], output: Path) -> None:
    selected = [item for item in run["threads"] if item.get("selected")]
    captured = [item for item in selected if item.get("capture_file")]
    lines = [
        "---",
        f'id: {yaml_quote("raw-reddit-" + run["run_id"] + "-corpus")}',
        'category: "raw-research"',
        f'title: {yaml_quote("Reddit corpus: " + run["topic"])}',
        f'capture_date: {yaml_quote(date.today().isoformat())}',
        f'run_id: {yaml_quote(run["run_id"])}',
        f'source_count: {len(captured)}',
        'evidence_status: "community-observation"',
        'tags: [reddit, deep-research, raw-corpus]',
        "---",
        "",
        f"# Reddit corpus: {run['topic']}",
        "",
        "> Community posts and comments are observations, not canonical facts. Verify critical claims against primary sources or local receipts.",
        "",
        "## Reproduction record",
        "",
        f"- Run ID: `{run['run_id']}`",
        f"- Query records: `{len(run['query_plan'])}`",
        f"- Unique discovered threads: `{len(run['threads'])}`",
        f"- Selected threads: `{len(selected)}`",
        f"- Captured threads: `{len(captured)}`",
        f"- Saturation reached: `{str(run['saturation']['reached']).lower()}`",
        f"- Retry summary: `{run_dir.as_posix()}/retry-summary.json`",
        f"- Run manifest: `{run_dir.as_posix()}/run.json`",
        f"- Query manifest: `{run_dir.as_posix()}/queries.json`",
        f"- Thread manifest: `{run_dir.as_posix()}/threads.json`",
        "",
        "## Discovery queries and exact search URLs",
        "",
    ]
    for query in run["query_plan"]:
        lines.append(f"- `{query['query']}` — [{query['sort']}]({query['search_url']}) — status `{query['status']}`, new unique `{query['new_unique_count']}`")
    lines.extend(["", "## Selected source URLs", ""])
    for item in selected:
        status = item["status"]
        quality = item.get("quality") or {}
        score = quality.get("score", "n/a")
        lines.append(f"- [{item['title']}]({item['canonical_url']}) — `{item['thread_id']}`, status `{status}`, quality `{score}`")
    lines.extend(["", "## Per-source capture digest", ""])
    for item in captured:
        capture = load_json(run_dir / item["capture_file"])
        lines.extend([
            f"### {capture.get('title') or item['title']}",
            "",
            f"- Reddit URL: {capture['canonical_url']}",
            f"- Capture file: `{run_dir.as_posix()}/{item['capture_file']}`",
            f"- Quality score: `{capture['quality']['score']}` (`{capture['quality']['method']}`)",
            f"- Captured comments: `{len(capture.get('comments', []))}`",
            f"- Outbound references: `{len(capture.get('outbound_references', []))}`",
            "",
            (capture.get("post_body") or "_No post body captured._")[:1500],
            "",
        ])
    dump_text(output, "\n".join(lines))


def render_synthesis(run_dir: Path, run: dict[str, Any], output: Path, minimum_score: float) -> None:
    selected = [item for item in run["threads"] if item.get("selected") and item.get("capture_file")]
    included = [item for item in selected if float((item.get("quality") or {}).get("score", 0)) >= minimum_score]
    domains = Counter()
    verification = Counter()
    query_support: dict[str, set[str]] = defaultdict(set)
    ledger_path = run_dir / "outbound-references.json"
    ledger = load_json(ledger_path) if ledger_path.exists() else {"references": []}
    for item in included:
        capture = load_json(run_dir / item["capture_file"])
        for query_id in capture.get("discovered_by_query_ids", []):
            query_support[query_id].add(item["thread_id"])
        for reference in capture.get("outbound_references", []):
            raw_url = reference.get("url") or reference.get("normalized_url") or ""
            host = re.sub(r"^www\.", "", re.sub(r"^https?://", "", raw_url).split("/")[0])
            if host:
                domains[host] += 1
    for reference in ledger.get("references", []):
        if reference.get("included", True):
            verification[reference.get("verification_state", "unverified")] += 1
    follow_up_path = run_dir / "follow-up.json"
    follow_up = load_json(follow_up_path) if follow_up_path.exists() else {}
    lines = [
        "---",
        f'id: {yaml_quote("raw-reddit-" + run["run_id"] + "-synthesis")}',
        'category: "raw-research-synthesis"',
        f'title: {yaml_quote("Reddit research synthesis: " + run["topic"])}',
        f'capture_date: {yaml_quote(date.today().isoformat())}',
        f'run_id: {yaml_quote(run["run_id"])}',
        f'source_count: {len(included)}',
        'evidence_status: "community-synthesis-unverified"',
        'tags: [reddit, deep-research, synthesis]',
        "---",
        "",
        f"# Reddit research synthesis: {run['topic']}",
        "",
        "> This document summarizes community evidence only. It intentionally does not promote observations to verified facts without primary-source or local-validation receipts.",
        "",
        "## Coverage",
        "",
        f"- Selected Reddit sources: `{sum(bool(item.get('selected')) for item in run['threads'])}`",
        f"- Successfully captured: `{len(selected)}`",
        f"- Included at quality score >= `{minimum_score}`: `{len(included)}`",
        f"- Failed or pending selected sources: `{sum(item.get('selected') and item['status'] not in {'captured', 'skipped'} for item in run['threads'])}`",
        f"- Saturation: `{str(run['saturation']['reached']).lower()}` — {run['saturation'].get('reason') or 'not recorded'}",
        "",
        "## Evidence inventory",
        "",
        "The following sources passed the deterministic inclusion threshold. Claims still require manual clustering and verification; the renderer does not infer consensus from raw text.",
        "",
    ]
    for item in sorted(included, key=lambda value: float(value["quality"]["score"]), reverse=True):
        lines.append(f"- [{item['title']}]({item['canonical_url']}) — quality `{item['quality']['score']}`, comments/capture in `{run_dir.as_posix()}/{item['capture_file']}`")
    lines.extend(["", "## Outbound reference verification", ""])
    if verification:
        for state, count in sorted(verification.items()):
            lines.append(f"- `{state}`: {count}")
    else:
        lines.append("- No outbound references captured.")
    if domains:
        lines.extend(["", "Top outbound domains:", ""])
        for domain, count in domains.most_common(15):
            lines.append(f"- `{domain}`: {count}")
    lines.extend(["", "## Confirmed facts", ""])
    facts = follow_up.get("confirmed_facts", [])
    lines.extend([f"- {value}" for value in facts] or ["- None recorded. Add only facts supported by verified primary sources or local receipts."])
    lines.extend(["", "## Community observations requiring verification", ""])
    lines.append("- Review the included source inventory and cluster repeated claims manually; preserve supporting thread URLs for every observation.")
    lines.extend(["", "## Identified bottlenecks", ""])
    lines.extend([f"- {value}" for value in follow_up.get("identified_bottlenecks", [])] or ["- None recorded."])
    lines.extend(["", "## New hypotheses", ""])
    lines.extend([f"- {value}" for value in follow_up.get("new_hypotheses", [])] or ["- None recorded."])
    lines.extend(["", "## Targeted follow-up queries", ""])
    lines.extend([f"- `{value}`" for value in follow_up.get("targeted_follow_up_queries", [])] or ["- None recorded."])
    lines.extend(["", "## Reproducibility artifacts", ""])
    for name in ("run.json", "queries.json", "threads.json", "outbound-references.json", "errors.jsonl", "follow-up.json"):
        lines.append(f"- `{run_dir.as_posix()}/{name}`")
    dump_text(output, "\n".join(lines))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    for command in ("corpus", "synthesis"):
        child = subparsers.add_parser(command)
        child.add_argument("--run-dir", required=True)
        child.add_argument("--output", required=True)
        if command == "synthesis":
            child.add_argument("--minimum-score", type=float, default=0.5)
    args = parser.parse_args()
    run_dir = Path(args.run_dir)
    output = Path(args.output)
    if output.name != kebab(output.stem) + ".md":
        parser.error("--output must use a kebab-case Markdown filename")
    run = load_json(run_dir / "run.json")
    if args.command == "corpus":
        render_corpus(run_dir, run, output)
    else:
        render_synthesis(run_dir, run, output, args.minimum_score)
    print(json.dumps({"output": output.as_posix(), "command": args.command}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
