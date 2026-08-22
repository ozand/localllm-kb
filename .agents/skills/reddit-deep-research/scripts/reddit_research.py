#!/usr/bin/env python3
"""Reproducible Reddit research batches driven through an authenticated Surf CLI tab.

The script writes durable JSON manifests and immutable per-thread JSON captures.
It never stores browser profiles, cookies, credentials, or absolute local paths.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import parse_qsl, quote, urlencode, urlsplit, urlunsplit

SCHEMA_VERSION = 1
DEFAULT_SUBREDDIT = "LocalLLaMA"
DEFAULT_SORTS = ("relevance", "top", "new")
TERMINAL_STATUSES = {"captured", "skipped"}
VERIFICATION_STATES = {"verified", "redirected", "unreachable", "failed", "skipped", "unverified"}
OUTBOUND_EXCLUDED_HOSTS = {
    "about:blank",
    "doubleclick.net",
    "google.com",
    "googletagmanager.com",
    "reddit.com",
    "redditstatic.com",
    "redditinc.com",
    "redd.it",
}
OUTBOUND_TRACKING_QUERY_KEYS = {"fbclid", "gclid", "ref", "ref_source", "source", "utm_campaign", "utm_content", "utm_medium", "utm_source", "utm_term"}
OUTBOUND_ASSET_SUFFIXES = (".css", ".gif", ".ico", ".jpeg", ".jpg", ".js", ".png", ".svg", ".webp", ".woff", ".woff2")
PRIMARY_OUTBOUND_HOSTS = {
    "github.com": 100,
    "gitlab.com": 95,
    "huggingface.co": 100,
    "huggingface.com": 100,
    "nvidia.com": 95,
    "developer.nvidia.com": 100,
}
SHELL_PAGE_TITLES = {"reddit - the heart of the internet", "reddit"}
CHROME_ONLY_LINES = {
    "advertise on reddit",
    "create",
    "create post",
    "expand user menu",
    "repost",
    "go to localllama",
    "r/localllama",
    "share",
    "openai",
    "collapse video player",
    "comments section",
}


class CaptureNotReadyError(RuntimeError):
    def __init__(self, reason: str):
        super().__init__(reason)
        self.reason = reason


def resolve_surf_executable() -> str:
    candidates = ["surf.cmd", "surf"] if os.name == "nt" else ["surf"]
    for candidate in candidates:
        resolved = shutil.which(candidate)
        if resolved:
            return resolved
    raise FileNotFoundError("Surf CLI not found; expected surf.cmd on Windows or surf on POSIX")


DISCOVERY_JS = r"""
return (() => {
  const posts = [];
  const seen = new Set();
  for (const a of Array.from(document.querySelectorAll('a[href*="/comments/"]'))) {
    const raw = a.href.split('#')[0].split('?')[0].replace(/\/$/, '') + '/';
    if (seen.has(raw) || !raw.includes('/comments/')) continue;
    const title = (a.innerText || a.textContent || '').trim();
    if (title.length < 8) continue;
    seen.add(raw);
    posts.push({title, url: raw});
  }
  return JSON.stringify(posts);
})();
"""

EXTRACT_JS = r"""
return (() => {
  const post = document.querySelector('shreddit-post');
  const title = document.querySelector('h1')?.innerText || document.title || '';
  const body = post?.getAttribute('post-text') ||
    post?.querySelector('[slot="text-body"]')?.innerText ||
    document.querySelector('div[data-click-id="text"]')?.innerText || '';
  const comments = Array.from(document.querySelectorAll('shreddit-comment')).slice(0, __COMMENT_LIMIT__).map(c => ({
    author: c.getAttribute('author') || 'anonymous',
    score: c.getAttribute('score') || '0',
    text: (c.innerText || '').trim().slice(0, 4000)
  })).filter(c => c.text.length > 20);
  const externalLinks = Array.from(document.querySelectorAll('a[href^="http"]'))
    .map(a => a.href.split('#')[0])
    .filter(h => !/reddit\.com|redd\.it|google\.com/.test(h));
  return JSON.stringify({
    canonical_url: window.location.href.split('#')[0].split('?')[0],
    title,
    author: post?.getAttribute('author') || null,
    has_post_element: Boolean(post),
    post_body: body.slice(0, 12000),
    comments,
    external_links: Array.from(new Set(externalLinks)).slice(0, 50)
  });
})();
"""


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def json_dump(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def json_load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def canonical_reddit_url(url: str) -> str:
    parts = urlsplit(url.strip())
    path = re.sub(r"/+", "/", parts.path)
    if "/comments/" not in path:
        return ""
    if not path.endswith("/"):
        path += "/"
    return urlunsplit(("https", "www.reddit.com", path, "", ""))


def slugify(value: str, max_length: int = 80) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    value = re.sub(r"-+", "-", value)
    return (value[:max_length].rstrip("-") or "reddit-thread")


def thread_id(url: str) -> str:
    match = re.search(r"/comments/([^/]+)/", url)
    return match.group(1) if match else hashlib.sha256(url.encode("utf-8")).hexdigest()[:12]


def parse_json_output(raw: str) -> Any:
    value: Any = json.loads(raw)
    if isinstance(value, str):
        value = json.loads(value)
    return value


def clean_extracted_text(value: str) -> str:
    lines = []
    for line in re.sub(r"\r\n?", "\n", value or "").split("\n"):
        normalized = re.sub(r"\s+", " ", line).strip()
        if not normalized or normalized.lower() in CHROME_ONLY_LINES:
            continue
        lines.append(normalized)
    return "\n".join(lines).strip()


def capture_readiness_reason(capture: dict[str, Any], min_body_chars: int = 20) -> str | None:
    title = clean_extracted_text(str(capture.get("title", "")))
    body = clean_extracted_text(str(capture.get("post_body", "")))
    canonical_url = canonical_reddit_url(str(capture.get("canonical_url", "")))
    if title.lower() in SHELL_PAGE_TITLES:
        return "shell-page-title"
    if not canonical_url:
        return "missing-reddit-url"
    if not capture.get("has_post_element", True):
        return "missing-post-element"
    if not title:
        return "missing-title"
    if not body:
        return "empty-post-body"
    if len(body) < min_body_chars:
        return "post-body-too-short"
    return None


def prepare_capture(capture: dict[str, Any], min_body_chars: int = 20) -> dict[str, Any]:
    prepared = dict(capture)
    prepared["title"] = clean_extracted_text(str(prepared.get("title", "")))
    prepared["post_body"] = clean_extracted_text(str(prepared.get("post_body", "")))
    reason = capture_readiness_reason(prepared, min_body_chars=min_body_chars)
    if reason:
        raise CaptureNotReadyError(reason)
    prepared["readiness"] = {"ready": True, "reason": None, "method": "reddit-dom-content-v1"}
    return prepared


def _windows_cmd_quote(value: str) -> str:
    escaped = value.replace('"', '\\"')
    if any(char in value for char in " &|<>^()"):
        return f'"{escaped}"'
    return escaped


def build_surf_invocation(tab: str, args: Iterable[str]) -> tuple[object, bool]:
    executable = resolve_surf_executable()
    command = [executable, "--tab", str(tab), *args]
    # npm installs Surf as a .cmd batch wrapper on Windows. Passing a list to
    # that wrapper can let cmd.exe reinterpret URL ampersands; explicitly quote
    # metacharacter-bearing arguments before shell dispatch.
    if os.name == "nt" and executable.lower().endswith((".cmd", ".bat")):
        return " ".join(_windows_cmd_quote(str(item)) for item in command), True
    return command, False


def run_surf(tab: str, args: Iterable[str], timeout: int = 90) -> str:
    command, use_shell = build_surf_invocation(tab, args)
    completed = subprocess.run(command, capture_output=True, text=True, timeout=timeout, check=False, shell=use_shell)
    if completed.returncode != 0:
        message = (completed.stderr or completed.stdout or "surf command failed").strip()
        raise RuntimeError(message[:500])
    return completed.stdout.strip()


def surf_js(tab: str, script: str, work_dir: Path, name: str) -> Any:
    script_dir = work_dir / "browser-scripts"
    script_dir.mkdir(parents=True, exist_ok=True)
    script_path = script_dir / f"{name}.js"
    script_path.write_text(script, encoding="utf-8")
    raw = run_surf(tab, ["js", "-f", str(script_path)])
    return parse_json_output(raw)


def query_record(subreddit: str, query: str, sort: str, time_filter: str | None) -> dict[str, Any]:
    search_url = (
        f"https://www.reddit.com/r/{subreddit}/search/?q={quote(query)}"
        f"&restrict_sr=1&sort={sort}"
    )
    if time_filter and sort == "top":
        search_url += f"&t={time_filter}"
    digest = hashlib.sha256(search_url.encode("utf-8")).hexdigest()[:12]
    return {
        "query_id": digest,
        "query": query,
        "subreddit": subreddit,
        "sort": sort,
        "time_filter": time_filter if sort == "top" else None,
        "search_url": search_url,
        "status": "pending",
        "attempts": 0,
        "discovered_count": 0,
        "new_unique_count": 0,
        "error": None,
    }


def new_run_manifest(args: argparse.Namespace, queries: list[str]) -> dict[str, Any]:
    if args.run_id != slugify(args.run_id, max_length=200):
        raise ValueError("--run-id must be lowercase kebab-case")
    created = utc_now()
    sorts = [item.strip() for item in args.sorts.split(",") if item.strip()]
    query_plan = [
        query_record(args.subreddit, query, sort, args.time_filter)
        for query in queries
        for sort in sorts
    ]
    return {
        "schema_version": SCHEMA_VERSION,
        "run_id": args.run_id,
        "topic": args.topic,
        "created_at": created,
        "updated_at": created,
        "status": "discovering",
        "target_selected_sources": args.target,
        "subreddits": [args.subreddit],
        "query_plan": query_plan,
        "selection_policy": {
            "deduplicate_by": "canonical_thread_url",
            "minimum_title_length": 8,
            "target_selected_sources": args.target,
            "ordering": "query-plan order, then DOM result order",
        },
        "threads": [],
        "counts": {"queries_total": len(query_plan), "queries_completed": 0, "discovered_unique": 0, "selected": 0, "captured": 0, "skipped": 0, "pending": 0, "errors": 0},
        "saturation": {
            "window_size": args.saturation_window,
            "minimum_new_sources": args.saturation_min_new,
            "consecutive_low_yield_queries": 0,
            "reached": False,
            "reason": None,
        },
        "artifacts": {
            "run_manifest": "run.json",
            "query_manifest": "queries.json",
            "thread_manifest": "threads.json",
            "errors": "errors.jsonl",
            "outbound_references": "outbound-references.json",
            "follow_up": "follow-up.json",
        },
    }


def write_derived_manifests(run_dir: Path, run: dict[str, Any]) -> None:
    json_dump(run_dir / "queries.json", {"schema_version": SCHEMA_VERSION, "run_id": run["run_id"], "queries": run["query_plan"]})
    json_dump(run_dir / "threads.json", {"schema_version": SCHEMA_VERSION, "run_id": run["run_id"], "threads": run["threads"]})
    json_dump(run_dir / "run.json", run)


def sanitize_diagnostic(message: str) -> str:
    sanitized = message.replace("\r", " ").replace("\n", " ")
    patterns = (
        (r"[A-Za-z]:[/\\][^\s\"']+", "<local-path>"),
        (r"(?<!:)\/(?:home|Users|tmp|var|opt|srv|mnt)\/[^\s\"']+", "<local-path>"),
        (r"(?i)(authorization|cookie|set-cookie|proxy-authorization)\s*[:=]\s*[^\s,;]+", r"\1=<redacted>"),
        (r"(?i)bearer\s+[A-Za-z0-9._~+\-/]+=*", "Bearer <redacted>"),
        (r"\bsk-[A-Za-z0-9_-]{8,}\b", "<redacted>"),
        (r"(?i)(api[_-]?key|access[_-]?token|refresh[_-]?token|password)\s*[:=]\s*[^\s,;]+", r"\1=<redacted>"),
    )
    for pattern, replacement in patterns:
        sanitized = re.sub(pattern, replacement, sanitized)
    return sanitized[:500]


def update_counts(run: dict[str, Any]) -> None:
    threads = run.get("threads", [])
    selected = [item for item in threads if item.get("selected")]
    run["counts"] = {
        "queries_total": len(run.get("query_plan", [])),
        "queries_completed": sum(item.get("status") == "completed" for item in run.get("query_plan", [])),
        "discovered_unique": len(threads),
        "selected": len(selected),
        "captured": sum(item.get("status") == "captured" for item in selected),
        "skipped": sum(item.get("status") == "skipped" for item in selected),
        "pending": sum(item.get("status") == "pending" for item in selected),
        "errors": sum(item.get("status") == "error" for item in selected),
    }


def append_error(run_dir: Path, stage: str, item_id: str, error_type: str, message: str, retryable: bool) -> None:
    receipt = {
        "schema_version": SCHEMA_VERSION,
        "timestamp": utc_now(),
        "stage": stage,
        "item_id": item_id,
        "error_type": error_type,
        "message": sanitize_diagnostic(message),
        "retryable": retryable,
    }
    with (run_dir / "errors.jsonl").open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(receipt, ensure_ascii=False) + "\n")


def discover(args: argparse.Namespace) -> int:
    run_dir = Path(args.run_dir)
    run_path = run_dir / "run.json"
    if run_path.exists():
        run = json_load(run_path)
    else:
        queries = [line.strip() for line in Path(args.queries_file).read_text(encoding="utf-8").splitlines() if line.strip() and not line.lstrip().startswith("#")]
        run = new_run_manifest(args, queries)
        write_derived_manifests(run_dir, run)

    known = {item["canonical_url"]: item for item in run["threads"]}
    low_yield = run["saturation"]["consecutive_low_yield_queries"]

    for query in run["query_plan"]:
        if query["status"] == "completed":
            continue
        if len(run["threads"]) >= run["target_selected_sources"]:
            break
        try:
            query["attempts"] += 1
            run_surf(args.tab, ["go", query["search_url"]], timeout=args.timeout)
            run_surf(args.tab, ["wait", str(args.wait_seconds)], timeout=args.timeout)
            for _ in range(args.scrolls):
                run_surf(args.tab, ["js", "window.scrollBy(0, 1800)"], timeout=args.timeout)
                run_surf(args.tab, ["wait", "1"], timeout=args.timeout)
            candidates = surf_js(args.tab, DISCOVERY_JS, run_dir, "discover-threads")
            new_count = 0
            for candidate in candidates:
                url = canonical_reddit_url(candidate.get("url", ""))
                if not url:
                    continue
                if url not in known:
                    record = {
                        "thread_id": thread_id(url),
                        "canonical_url": url,
                        "title": candidate.get("title", "").strip(),
                        "discovered_by_query_ids": [query["query_id"]],
                        "selected": len(run["threads"]) < run["target_selected_sources"],
                        "selection_reason": "first unique canonical URL in deterministic query order",
                        "status": "pending",
                        "attempts": 0,
                        "capture_file": None,
                        "quality": None,
                        "outbound_reference_count": 0,
                        "last_error": None,
                    }
                    run["threads"].append(record)
                    known[url] = record
                    new_count += 1
                elif query["query_id"] not in known[url]["discovered_by_query_ids"]:
                    known[url]["discovered_by_query_ids"].append(query["query_id"])
            query.update({"status": "completed", "discovered_count": len(candidates), "new_unique_count": new_count, "error": None})
            low_yield = low_yield + 1 if new_count < run["saturation"]["minimum_new_sources"] else 0
        except Exception as exc:  # noqa: BLE001
            query.update({"status": "error", "error": str(exc)[:300]})
            append_error(run_dir, "discovery", query["query_id"], type(exc).__name__, str(exc), True)
        run["saturation"]["consecutive_low_yield_queries"] = low_yield
        if low_yield >= run["saturation"]["window_size"]:
            run["saturation"].update({"reached": True, "reason": "consecutive discovery queries yielded fewer than the configured minimum new sources"})
            break
        run["updated_at"] = utc_now()
        update_counts(run)
        write_derived_manifests(run_dir, run)

    run["status"] = "discovered"
    run["updated_at"] = utc_now()
    update_counts(run)
    write_derived_manifests(run_dir, run)
    print(json.dumps({"run_id": run["run_id"], "selected": run["counts"]["selected"], "discovered_unique": run["counts"]["discovered_unique"], "saturation": run["saturation"]}, ensure_ascii=False))
    return 0 if run["counts"]["selected"] >= run["target_selected_sources"] or run["saturation"]["reached"] else 3


def score_capture(capture: dict[str, Any], keywords: list[str]) -> dict[str, Any]:
    combined = " ".join([capture.get("title", ""), capture.get("post_body", ""), *[item.get("text", "") for item in capture.get("comments", [])]]).lower()
    evidence_terms = ["tok/s", "tokens/s", "vram", "gb", "context", "watt", "power limit", "temperature", "command", "--"]
    evidence_hits = sum(term in combined for term in evidence_terms)
    relevance_hits = sum(term.lower() in combined for term in keywords)
    scrutiny = min(len(capture.get("comments", [])) / 10.0, 1.0)
    evidence = min(evidence_hits / 5.0, 1.0)
    relevance = min(relevance_hits / max(len(keywords), 1), 1.0)
    total = round(0.45 * evidence + 0.35 * relevance + 0.20 * scrutiny, 3)
    return {"score": total, "evidence": round(evidence, 3), "relevance": round(relevance, 3), "community_scrutiny": round(scrutiny, 3), "method": "deterministic-keyword-v1"}


def normalize_outbound_url(value: str) -> tuple[str | None, str | None]:
    original = str(value or "").strip()
    try:
        parts = urlsplit(original)
    except ValueError:
        return None, "invalid-url"
    if parts.scheme.lower() not in {"http", "https"}:
        return None, "invalid-scheme"
    if not parts.hostname or parts.username or parts.password:
        return None, "private-or-missing-host"
    host = parts.hostname.lower().rstrip(".")
    if host in OUTBOUND_EXCLUDED_HOSTS or any(host.endswith("." + suffix) for suffix in OUTBOUND_EXCLUDED_HOSTS if "." in suffix):
        return None, "excluded-domain"
    if parts.path.lower().endswith(OUTBOUND_ASSET_SUFFIXES):
        return None, "static-asset"
    try:
        query = [(key, val) for key, val in parse_qsl(parts.query, keep_blank_values=True) if key.lower() not in OUTBOUND_TRACKING_QUERY_KEYS]
    except ValueError:
        return None, "invalid-query"
    port = parts.port
    netloc = host
    if port and not ((parts.scheme.lower() == "http" and port == 80) or (parts.scheme.lower() == "https" and port == 443)):
        netloc = f"{host}:{port}"
    normalized = urlunsplit((parts.scheme.lower(), netloc, parts.path or "/", urlencode(sorted(query)), ""))
    return normalized, None


def score_outbound_url(normalized_url: str) -> tuple[int, str]:
    parts = urlsplit(normalized_url)
    host = parts.hostname or ""
    for primary_host, score in PRIMARY_OUTBOUND_HOSTS.items():
        if host == primary_host or host.endswith("." + primary_host):
            return score, "primary"
    if host.startswith("docs.") or host.startswith("developer.") or "/docs" in parts.path.lower() or "/issues" in parts.path.lower() or "/releases" in parts.path.lower():
        return 80, "technical-documentation"
    if any(token in normalized_url.lower() for token in ("llama.cpp", "llamacpp", "vllm", "unsloth", "gguf", "quant")):
        return 70, "llm-technical"
    return 40, "other-public"


def prepare_outbound_reference(url: str, thread_id_value: str, capture_file: str | None) -> dict[str, Any]:
    normalized, reason = normalize_outbound_url(url)
    if reason:
        return {
            "original_urls": [url],
            "normalized_url": None,
            "source_thread_ids": [thread_id_value],
            "source_capture_files": [capture_file] if capture_file else [],
            "included": False,
            "filter_reason": reason,
            "priority_score": 0,
            "priority_class": "excluded",
            "verification_state": "skipped",
            "verified_at": None,
            "final_url": None,
            "note": None,
        }
    priority_score, priority_class = score_outbound_url(normalized)
    return {
        "original_urls": [url],
        "normalized_url": normalized,
        "source_thread_ids": [thread_id_value],
        "source_capture_files": [capture_file] if capture_file else [],
        "included": True,
        "filter_reason": None,
        "priority_score": priority_score,
        "priority_class": priority_class,
        "verification_state": "unverified",
        "verified_at": None,
        "final_url": None,
        "note": None,
    }


def build_outbound_ledger(run_dir: Path, run: dict[str, Any]) -> dict[str, Any]:
    ledger_path = run_dir / "outbound-references.json"
    existing_by_url: dict[str, dict[str, Any]] = {}
    if ledger_path.exists():
        for reference in json_load(ledger_path).get("references", []):
            if reference.get("normalized_url"):
                existing_by_url[reference["normalized_url"]] = reference
    merged: dict[str, dict[str, Any]] = {}
    excluded: list[dict[str, Any]] = []
    for item in run["threads"]:
        if not item.get("capture_file"):
            continue
        capture = json_load(run_dir / item["capture_file"])
        for raw_reference in capture.get("outbound_references", []):
            url = raw_reference.get("url") or raw_reference.get("original_url")
            prepared = prepare_outbound_reference(url, item["thread_id"], item["capture_file"])
            normalized = prepared["normalized_url"]
            if not normalized:
                prepared["reference_id"] = f"excluded-{hashlib.sha256(str(url).encode('utf-8')).hexdigest()[:12]}"
                excluded.append(prepared)
                continue
            if normalized not in merged:
                prior = existing_by_url.get(normalized, {})
                merged[normalized] = {
                    **prepared,
                    **{key: prior[key] for key in ("verification_state", "verified_at", "final_url", "note") if key in prior},
                    "original_urls": list(prior.get("original_urls", [])),
                    "source_thread_ids": list(prior.get("source_thread_ids", [])),
                    "source_capture_files": list(prior.get("source_capture_files", [])),
                }
            current = merged[normalized]
            for key, value in (("original_urls", url), ("source_thread_ids", item["thread_id"]), ("source_capture_files", item["capture_file"])):
                if value and value not in current[key]:
                    current[key].append(value)
    included = []
    for normalized, reference in merged.items():
        reference["reference_id"] = "outbound-" + hashlib.sha256(normalized.encode("utf-8")).hexdigest()[:12]
        reference["source_count"] = len(reference["source_thread_ids"])
        included.append(reference)
    included.sort(key=lambda value: (-value["priority_score"], value["normalized_url"]))
    excluded.sort(key=lambda value: (value["filter_reason"], value["reference_id"]))
    return {"schema_version": SCHEMA_VERSION, "run_id": run["run_id"], "references": included + excluded}


def extract(args: argparse.Namespace) -> int:
    run_dir = Path(args.run_dir)
    run = json_load(run_dir / "run.json")
    raw_dir = run_dir / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    keywords = [item.strip() for item in args.keywords.split(",") if item.strip()]
    processed = 0

    for item in run["threads"]:
        if not item.get("selected") or item["status"] in TERMINAL_STATUSES:
            continue
        if args.limit and processed >= args.limit:
            break
        try:
            item["attempts"] += 1
            run_surf(args.tab, ["go", item["canonical_url"]], timeout=args.timeout)
            run_surf(args.tab, ["wait", str(args.wait_seconds)], timeout=args.timeout)
            script = EXTRACT_JS.replace("__COMMENT_LIMIT__", str(args.comment_limit))
            capture = surf_js(args.tab, script, run_dir, "extract-thread")
            capture = prepare_capture(capture)
            capture.update({
                "schema_version": SCHEMA_VERSION,
                "run_id": run["run_id"],
                "thread_id": item["thread_id"],
                "source_type": "reddit-thread",
                "captured_at": utc_now(),
                "discovered_by_query_ids": item["discovered_by_query_ids"],
            })
            capture["quality"] = score_capture(capture, keywords)
            capture["outbound_references"] = [
                {"url": url, "verification_state": "unverified", "verified_at": None, "final_url": None, "note": "captured from Reddit DOM; filtering and verification are separate stages"}
                for url in capture.pop("external_links", [])
            ]
            filename = f"{item['thread_id']}-{slugify(capture.get('title', item['title']))}.json"
            capture_path = raw_dir / filename
            if not capture_path.exists():
                json_dump(capture_path, capture)
            item.update({
                "status": "captured",
                "capture_file": f"raw/{filename}",
                "quality": capture["quality"],
                "outbound_reference_count": len(capture["outbound_references"]),
                "last_error": None,
            })
        except CaptureNotReadyError as exc:
            item.update({"status": "error", "last_error": {"type": type(exc).__name__, "reason": exc.reason}})
            append_error(run_dir, "extraction", item["thread_id"], type(exc).__name__, exc.reason, False)
        except Exception as exc:  # noqa: BLE001
            item.update({"status": "error", "last_error": {"type": type(exc).__name__, "message": sanitize_diagnostic(str(exc))}})
            append_error(run_dir, "extraction", item["thread_id"], type(exc).__name__, str(exc), True)
        processed += 1
        run["updated_at"] = utc_now()
        update_counts(run)
        write_derived_manifests(run_dir, run)

    run["status"] = "captured" if all((not item.get("selected")) or item["status"] in TERMINAL_STATUSES for item in run["threads"]) else "partial"
    json_dump(run_dir / "outbound-references.json", build_outbound_ledger(run_dir, run))
    follow_up_path = run_dir / "follow-up.json"
    if not follow_up_path.exists():
        json_dump(follow_up_path, {
            "schema_version": SCHEMA_VERSION,
            "run_id": run["run_id"],
            "confirmed_facts": [],
            "identified_bottlenecks": [],
            "new_hypotheses": [],
            "targeted_follow_up_queries": [],
            "note": "Populate after synthesis; empty lists are intentional and auditable.",
        })
    run["updated_at"] = utc_now()
    update_counts(run)
    write_derived_manifests(run_dir, run)
    print(json.dumps({"run_id": run["run_id"], "status": run["status"], **run["counts"]}, ensure_ascii=False))
    return 0 if run["status"] == "captured" else 4


def skip_thread(args: argparse.Namespace) -> int:
    run_dir = Path(args.run_dir)
    run = json_load(run_dir / "run.json")
    matches = [item for item in run["threads"] if item.get("thread_id") == args.thread_id and item.get("selected")]
    if not matches:
        print(json.dumps({"error": "selected-thread-not-found", "thread_id": args.thread_id}), file=sys.stderr)
        return 2
    item = matches[0]
    if item.get("status") == "captured":
        print(json.dumps({"error": "immutable-capture-exists", "thread_id": args.thread_id}), file=sys.stderr)
        return 2
    item.update({
        "status": "skipped",
        "skip_reason": args.reason,
        "skipped_at": utc_now(),
        "last_error": None,
    })
    run["updated_at"] = utc_now()
    update_counts(run)
    run["status"] = "captured" if run["counts"]["pending"] == 0 and run["counts"]["errors"] == 0 else "partial"
    write_derived_manifests(run_dir, run)
    print(json.dumps({"run_id": run["run_id"], "thread_id": args.thread_id, "status": "skipped", "reason": args.reason}, ensure_ascii=False))
    return 0


def verify_outbound(args: argparse.Namespace) -> int:
    run_dir = Path(args.run_dir)
    run = json_load(run_dir / "run.json")
    ledger_path = run_dir / "outbound-references.json"
    ledger = build_outbound_ledger(run_dir, run)
    json_dump(ledger_path, ledger)
    checked = 0
    for reference in ledger["references"]:
        if not reference.get("included") or reference.get("verification_state") != "unverified":
            continue
        if args.limit and checked >= args.limit:
            break
        checked += 1
        original = reference["normalized_url"]
        try:
            run_surf(args.tab, ["go", original], timeout=args.timeout)
            run_surf(args.tab, ["wait", str(args.wait_seconds)], timeout=args.timeout)
            final_url = run_surf(args.tab, ["js", "return window.location.href"], timeout=args.timeout)
            try:
                final_url = json.loads(final_url)
            except json.JSONDecodeError:
                final_url = final_url.strip('"')
            reference.update({
                "verification_state": "redirected" if final_url and final_url != original else "unverified",
                "accessed_at": utc_now(),
                "final_url": final_url or original,
                "note": args.note or "Target loaded through Surf; evidence inspection and manual verification are still required.",
            })
        except Exception as exc:  # noqa: BLE001
            reference.update({
                "verification_state": "failed",
                "accessed_at": utc_now(),
                "final_url": None,
                "note": f"Sanitized access failure: {type(exc).__name__}",
            })
            append_error(run_dir, "outbound-verification", reference.get("reference_id", reference.get("thread_id", "unknown")), type(exc).__name__, str(exc), True)
        json_dump(ledger_path, ledger)
    counts = {state: sum(ref.get("verification_state") == state for ref in ledger["references"] if ref.get("included")) for state in sorted(VERIFICATION_STATES)}
    print(json.dumps({"run_id": run["run_id"], "checked": checked, "verification_counts": counts}, ensure_ascii=False))
    return 0


def mark_outbound(args: argparse.Namespace) -> int:
    run_dir = Path(args.run_dir)
    run = json_load(run_dir / "run.json")
    ledger_path = run_dir / "outbound-references.json"
    ledger = build_outbound_ledger(run_dir, run)
    matches = [item for item in ledger["references"] if item.get("reference_id") == args.reference_id and item.get("included")]
    if not matches:
        print(json.dumps({"error": "reference-not-found", "reference_id": args.reference_id}), file=sys.stderr)
        return 2
    reference = matches[0]
    reference.update({
        "verification_state": args.state,
        "verified_at": utc_now(),
        "final_url": args.final_url or reference.get("final_url") or reference["normalized_url"],
        "note": args.note,
    })
    json_dump(ledger_path, ledger)
    print(json.dumps({"run_id": run["run_id"], "reference_id": args.reference_id, "verification_state": args.state}, ensure_ascii=False))
    return 0


def write_receipt(args: argparse.Namespace) -> int:
    run_dir = Path(args.run_dir)
    run = json_load(run_dir / "run.json")
    update_counts(run)
    ledger_path = run_dir / "outbound-references.json"
    ledger = json_load(ledger_path) if ledger_path.exists() else {"references": []}
    verification_counts = {state: sum(ref.get("verification_state") == state for ref in ledger["references"] if ref.get("included")) for state in sorted(VERIFICATION_STATES)}
    receipt = {
        "schema_version": SCHEMA_VERSION,
        "skill_used": "reddit-deep-research",
        "run_id": run["run_id"],
        "run_directory": Path(args.run_dir).as_posix(),
        "status": run.get("status"),
        "counts": run["counts"],
        "target_selected_sources": run.get("target_selected_sources"),
        "saturation": run.get("saturation"),
        "scripts": [
            ".agents/skills/reddit-deep-research/scripts/reddit_research.py",
            ".agents/skills/reddit-deep-research/scripts/render_research.py",
        ],
        "artifacts": run.get("artifacts", {}),
        "outbound_verification_counts": verification_counts,
        "complete": run["counts"]["pending"] == 0 and run["counts"]["errors"] == 0 and (run["counts"]["selected"] >= run.get("target_selected_sources", 0) or bool(run.get("saturation", {}).get("reached"))),
        "residual_risks": [
            "Reddit captures are community observations, not canonical facts.",
            "Outbound references marked unverified still require manual evidence inspection.",
        ],
    }
    json_dump(Path(args.output), receipt)
    print(json.dumps(receipt, ensure_ascii=False))
    return 0 if receipt["complete"] else 4


def validate(args: argparse.Namespace) -> int:
    run_dir = Path(args.run_dir)
    problems: list[str] = []
    run = json_load(run_dir / "run.json")
    update_counts(run)
    if run.get("run_id") != slugify(str(run.get("run_id", "")), max_length=200):
        problems.append("run_id is not lowercase kebab-case")
    query_ids = {item["query_id"] for item in run.get("query_plan", [])}
    urls = [item["canonical_url"] for item in run.get("threads", [])]
    if len(urls) != len(set(urls)):
        problems.append("duplicate canonical thread URLs")
    if not query_ids:
        problems.append("query plan is empty")
    for item in run.get("threads", []):
        if not item.get("discovered_by_query_ids"):
            problems.append(f"thread {item.get('thread_id')} has no query provenance")
        if not set(item.get("discovered_by_query_ids", [])).issubset(query_ids):
            problems.append(f"thread {item.get('thread_id')} references an unknown query id")
        capture_file = item.get("capture_file")
        if capture_file:
            capture_path = run_dir / capture_file
            if not capture_path.exists():
                problems.append(f"missing capture {capture_file}")
            elif capture_path.name != slugify(capture_path.stem, max_length=200) + ".json":
                problems.append(f"capture is not kebab-case: {capture_path.name}")
            else:
                capture = json_load(capture_path)
                for field in ("canonical_url", "captured_at", "quality", "discovered_by_query_ids"):
                    if field not in capture:
                        problems.append(f"capture {capture_file} lacks {field}")
                for reference in capture.get("outbound_references", []):
                    if reference.get("verification_state") not in VERIFICATION_STATES:
                        problems.append(f"capture {capture_file} has invalid outbound verification state")
    selected = [item for item in run.get("threads", []) if item.get("selected")]
    incomplete = [item for item in selected if item.get("status") not in TERMINAL_STATUSES]
    if incomplete:
        problems.append(f"selected extraction incomplete: {run['counts']['pending']} pending, {run['counts']['errors']} errors")
    if args.require_target and len(selected) < run.get("target_selected_sources", 0) and not run.get("saturation", {}).get("reached"):
        problems.append("selected source target not met and saturation not reached")
    result = {"valid": not problems, "problems": problems, "run_id": run.get("run_id")}
    print(json.dumps(result, ensure_ascii=False))
    return 0 if not problems else 2


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    discover_parser = subparsers.add_parser("discover", help="Run deterministic Reddit search discovery and persist query/thread manifests.")
    discover_parser.add_argument("--tab", required=True, help="Existing authenticated Surf tab id.")
    discover_parser.add_argument("--topic", required=True)
    discover_parser.add_argument("--run-id", required=True, help="Stable kebab-case research run identifier.")
    discover_parser.add_argument("--run-dir", required=True)
    discover_parser.add_argument("--queries-file", required=True, help="UTF-8 file containing one query per line.")
    discover_parser.add_argument("--subreddit", default=DEFAULT_SUBREDDIT)
    discover_parser.add_argument("--sorts", default=",".join(DEFAULT_SORTS))
    discover_parser.add_argument("--time-filter", default="year")
    discover_parser.add_argument("--target", type=int, default=50)
    discover_parser.add_argument("--scrolls", type=int, default=2)
    discover_parser.add_argument("--wait-seconds", type=int, default=2)
    discover_parser.add_argument("--timeout", type=int, default=90)
    discover_parser.add_argument("--saturation-window", type=int, default=5)
    discover_parser.add_argument("--saturation-min-new", type=int, default=2)
    discover_parser.set_defaults(func=discover)

    extract_parser = subparsers.add_parser("extract", help="Resume extraction for selected pending/error threads and write immutable JSON captures.")
    extract_parser.add_argument("--tab", required=True)
    extract_parser.add_argument("--run-dir", required=True)
    extract_parser.add_argument("--keywords", default="benchmark,configuration,vram,context,tokens,temperature,power")
    extract_parser.add_argument("--comment-limit", type=int, default=15)
    extract_parser.add_argument("--limit", type=int, default=0, help="Maximum threads this invocation; 0 means all remaining.")
    extract_parser.add_argument("--wait-seconds", type=int, default=2)
    extract_parser.add_argument("--timeout", type=int, default=90)
    extract_parser.set_defaults(func=extract)

    skip_parser = subparsers.add_parser("skip", help="Explicitly skip one selected uncaptured thread with a durable reason.")
    skip_parser.add_argument("--run-dir", required=True)
    skip_parser.add_argument("--thread-id", required=True)
    skip_parser.add_argument("--reason", required=True)
    skip_parser.set_defaults(func=skip_thread)

    verify_parser = subparsers.add_parser("verify-outbound", help="Visit unverified outbound references through Surf and persist verification states.")
    verify_parser.add_argument("--tab", required=True)
    verify_parser.add_argument("--run-dir", required=True)
    verify_parser.add_argument("--limit", type=int, default=0, help="Maximum unverified references this invocation; 0 means all.")
    verify_parser.add_argument("--wait-seconds", type=int, default=2)
    verify_parser.add_argument("--timeout", type=int, default=90)
    verify_parser.add_argument("--note", default="", help="Manual evidence note. A successful load remains unverified unless reviewed separately.")
    verify_parser.set_defaults(func=verify_outbound)

    mark_parser = subparsers.add_parser("mark-outbound", help="Record a manually inspected outbound reference state and evidence note.")
    mark_parser.add_argument("--run-dir", required=True)
    mark_parser.add_argument("--reference-id", required=True)
    mark_parser.add_argument("--state", required=True, choices=("verified", "redirected", "failed", "skipped"))
    mark_parser.add_argument("--note", required=True)
    mark_parser.add_argument("--final-url", default="")
    mark_parser.set_defaults(func=mark_outbound)

    receipt_parser = subparsers.add_parser("receipt", help="Write an auditable JSON completion receipt with honest source and error counts.")
    receipt_parser.add_argument("--run-dir", required=True)
    receipt_parser.add_argument("--output", required=True)
    receipt_parser.set_defaults(func=write_receipt)

    validate_parser = subparsers.add_parser("validate", help="Validate manifest provenance, deduplication, captures, and outbound states.")
    validate_parser.add_argument("--run-dir", required=True)
    validate_parser.add_argument("--require-target", action="store_true")
    validate_parser.set_defaults(func=validate)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        return args.func(args)
    except FileNotFoundError as exc:
        print(json.dumps({"error": "file-not-found", "message": str(exc)}), file=sys.stderr)
        return 2
    except subprocess.TimeoutExpired as exc:
        print(json.dumps({"error": "timeout", "message": str(exc)}), file=sys.stderr)
        return 5


if __name__ == "__main__":
    raise SystemExit(main())
