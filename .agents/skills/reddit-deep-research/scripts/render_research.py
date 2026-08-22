#!/usr/bin/env python3
"""Render an auditable Reddit research run as OKF Markdown without inventing facts."""

from __future__ import annotations

import argparse
import hashlib
import ipaddress
import json
import re
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

CLAIM_REVIEW_VERSION = "claim-review-v1"
CLAIM_RELATIONSHIPS = {"duplicate", "compatible", "conflicting", "unresolved"}


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


def normalize_claim_text(value: Any) -> str:
    text = re.sub(r"\s+", " ", str(value or "").strip().lower())
    text = re.sub(r"https?://\S+", "<url>", text)
    return text[:4000]


def claim_cluster_key(claim: dict[str, Any]) -> tuple[str, str]:
    explicit = normalize_claim_text(claim.get("cluster_key"))
    if explicit:
        return explicit, "explicit-cluster-key"
    normalized = normalize_claim_text(claim.get("text"))
    without_numbers = re.sub(r"\b\d+(?:[.,]\d+)?\b", "<number>", normalized)
    digest = hashlib.sha256(without_numbers.encode("utf-8")).hexdigest()[:16]
    return "derived-" + digest, "normalized-claim-text"


def public_source_urls(values: Any) -> tuple[list[str], list[str]]:
    if not isinstance(values, list):
        return [], ["source_urls must be a list"]
    valid = []
    errors = []
    for value in values:
        url = str(value or "").strip()
        try:
            parts = urlsplit(url)
        except ValueError:
            parts = None
        host = (parts.hostname or "").lower() if parts else ""
        if not parts or parts.scheme != "https" or not host or parts.username or parts.password:
            errors.append("source URL must be an https URL without credentials")
            continue
        try:
            private_host = ipaddress.ip_address(host).is_private
        except ValueError:
            private_host = False
        if private_host or host in {"localhost", "127.0.0.1", "::1"} or host.endswith((".local", ".internal")):
            errors.append("private source URL is not eligible for promotion")
            continue
        if url not in valid:
            valid.append(url)
    return valid, errors


def comparable_value(claim: dict[str, Any]) -> str:
    value = claim.get("value")
    if value is None:
        value = claim.get("polarity")
    return normalize_claim_text(value)


def prepare_claim(claim: Any, index: int) -> dict[str, Any]:
    raw = claim if isinstance(claim, dict) else {}
    text = normalize_claim_text(raw.get("text"))
    claim_id = normalize_claim_text(raw.get("claim_id")) or f"claim-{index + 1}"
    cluster_key, grouping_reason = claim_cluster_key(raw)
    source_urls, source_errors = public_source_urls(raw.get("source_urls", []))
    return {
        "claim_id": claim_id,
        "text": text,
        "cluster_key": cluster_key,
        "grouping_reason": grouping_reason,
        "value": normalize_claim_text(raw.get("value")),
        "polarity": normalize_claim_text(raw.get("polarity")),
        "source_urls": source_urls,
        "source_errors": source_errors,
        "promotion_candidate": bool(raw.get("promotion_candidate", True)),
    }


def relationship(left: dict[str, Any], right: dict[str, Any]) -> tuple[str, str]:
    left_value = comparable_value(left)
    right_value = comparable_value(right)
    if left["text"] and left["text"] == right["text"] and left_value == right_value:
        return "duplicate", "normalized claim text and comparable value are identical"
    if not left_value or not right_value:
        return "unresolved", "claims share a cluster but lack comparable values"
    if left_value == right_value:
        return "compatible", "claims share a cluster and comparable values"
    return "conflicting", "claims share a cluster but comparable values differ"


def validate_promotion(claim: dict[str, Any], relationships: list[dict[str, Any]], review_complete: bool) -> dict[str, Any]:
    reasons = []
    if not review_complete:
        reasons.append("claim review is incomplete")
    if claim.get("promotion_candidate") and not claim.get("source_urls"):
        reasons.append("missing exact public source URL")
    if claim.get("source_errors"):
        reasons.extend(claim["source_errors"])
    related = [item for item in relationships if claim["claim_id"] in {item["left_claim_id"], item["right_claim_id"]}]
    if any(item["relationship"] in {"conflicting", "unresolved"} for item in related):
        reasons.append("contradiction review has conflicting or unresolved relationships")
    return {"eligible": not reasons, "reasons": reasons}


def analyze_claims(raw_claims: Any) -> dict[str, Any]:
    claims_input = raw_claims.get("claims", []) if isinstance(raw_claims, dict) else raw_claims
    if not isinstance(claims_input, list):
        raise ValueError("claims input must be a list or an object with a claims list")
    claims = [prepare_claim(item, index) for index, item in enumerate(claims_input)]
    groups = defaultdict(list)
    for claim in claims:
        groups[claim["cluster_key"]].append(claim)
    relationships = []
    for group in groups.values():
        for index, left in enumerate(group):
            for right in group[index + 1:]:
                relation, reason = relationship(left, right)
                relationships.append({
                    "left_claim_id": left["claim_id"],
                    "right_claim_id": right["claim_id"],
                    "cluster_key": left["cluster_key"],
                    "relationship": relation,
                    "reason": reason,
                })
    review_complete = bool(claims)
    for claim in claims:
        related = validate_promotion(claim, relationships, review_complete)
        claim["promotion"] = related
    counts = {relation: sum(item["relationship"] == relation for item in relationships) for relation in sorted(CLAIM_RELATIONSHIPS)}
    return {
        "schema_version": CLAIM_REVIEW_VERSION,
        "review_status": "complete" if review_complete else "empty",
        "promotion_ready": bool(claims) and all(item["promotion"]["eligible"] for item in claims if item["promotion_candidate"]),
        "claim_count": len(claims),
        "cluster_count": len(groups),
        "relationship_counts": counts,
        "claims": claims,
        "relationships": relationships,
    }


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
            f"- Ranked comments: `{capture.get('comment_ranking', {}).get('comment_count', 0)}`",
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
    claim_review = analyze_claims(follow_up.get("claims", []))
    claim_review_path = run_dir / "claim-review.json"
    dump_text(claim_review_path, json.dumps(claim_review, ensure_ascii=False, indent=2))
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
        f"- Claim review: `{claim_review['review_status']}`; clusters `{claim_review['cluster_count']}`; promotion ready `{str(claim_review['promotion_ready']).lower()}`",
        f"- Claim review artifact: `{claim_review_path.as_posix()}`",
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
    lines.extend(["", "## Claim review", ""])
    lines.append(f"- Review version: `{claim_review['schema_version']}`")
    lines.append(f"- Relationship counts: `{json.dumps(claim_review['relationship_counts'], sort_keys=True)}`")
    lines.append("- Claims with missing, private, conflicting, or unresolved evidence remain blocked from promotion; this pass does not adjudicate truth.")
    for claim in claim_review["claims"]:
        lines.append(f"- `{claim['claim_id']}` / cluster `{claim['cluster_key']}` — promotion `{str(claim['promotion']['eligible']).lower()}` — sources `{', '.join(claim['source_urls']) or 'none'}`")
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
    for name in ("run.json", "queries.json", "threads.json", "retry-summary.json", "claim-review.json", "outbound-references.json", "errors.jsonl", "follow-up.json"):
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
