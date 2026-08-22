import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / ".agents" / "skills" / "reddit-deep-research"
FIXTURE = ROOT / "tests" / "fixtures" / "reddit-research-run"


def load_script(name: str):
    path = SKILL / "scripts" / name
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_skill_structure_and_metadata():
    text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    assert len(text.splitlines()) < 500
    assert "Use this skill when" in text
    assert "C:/Temp" in text
    assert (SKILL / "references" / "artifact-contract.md").exists()
    assert (SKILL / "references" / "research-methodology.md").exists()
    evals = json.loads((SKILL / "evals" / "evals.json").read_text(encoding="utf-8"))
    assert len(evals["cases"]) == 3


def test_validator_accepts_auditable_fixture():
    script = SKILL / "scripts" / "reddit_research.py"
    result = subprocess.run(
        [sys.executable, str(script), "validate", "--run-dir", str(FIXTURE), "--require-target"],
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr + result.stdout
    assert json.loads(result.stdout)["valid"] is True


def test_renderer_outputs_okf_and_exact_urls(tmp_path):
    script = SKILL / "scripts" / "render_research.py"
    corpus = tmp_path / "fixture-reddit-run-corpus.md"
    synthesis = tmp_path / "fixture-reddit-run-synthesis.md"
    subprocess.run([sys.executable, str(script), "corpus", "--run-dir", str(FIXTURE), "--output", str(corpus)], check=True)
    subprocess.run([sys.executable, str(script), "synthesis", "--run-dir", str(FIXTURE), "--output", str(synthesis)], check=True)
    corpus_text = corpus.read_text(encoding="utf-8")
    synthesis_text = synthesis.read_text(encoding="utf-8")
    assert corpus_text.startswith("---\n")
    assert "run_id:" in corpus_text and "source_count:" in corpus_text and "evidence_status:" in corpus_text
    assert "https://www.reddit.com/r/LocalLLaMA/search/" in corpus_text
    assert "https://www.reddit.com/r/LocalLLaMA/comments/abc123/fixture/" in corpus_text
    assert "community-synthesis-unverified" in synthesis_text
    assert re.fullmatch(r"[a-z0-9-]+\.md", corpus.name)


def test_resume_contract_excludes_successful_captures():
    module = load_script("reddit_research.py")
    assert module.TERMINAL_STATUSES == {"captured", "skipped"}


def test_validator_rejects_partial_selected_extraction(tmp_path):
    run = json.loads((FIXTURE / "run.json").read_text(encoding="utf-8"))
    run["threads"][0]["status"] = "error"
    run["threads"][0]["capture_file"] = None
    run["counts"].update({"captured": 0, "errors": 1})
    (tmp_path / "run.json").write_text(json.dumps(run), encoding="utf-8")
    script = SKILL / "scripts" / "reddit_research.py"
    result = subprocess.run([sys.executable, str(script), "validate", "--run-dir", str(tmp_path), "--require-target"], capture_output=True, text=True)
    assert result.returncode != 0
    assert "selected extraction incomplete" in result.stdout


def test_resolves_windows_npm_cmd_wrapper():
    module = load_script("reddit_research.py")
    resolved = module.resolve_surf_executable()
    assert resolved.lower().endswith(("surf.cmd", "surf"))


def test_windows_cmd_invocation_quotes_ampersand_url(monkeypatch):
    module = load_script("reddit_research.py")
    monkeypatch.setattr(module.os, "name", "nt")
    monkeypatch.setattr(module, "resolve_surf_executable", lambda: "C:/npm/surf.cmd")
    command, use_shell = module.build_surf_invocation("366714952", ["go", "https://www.reddit.com/r/LocalLLaMA/search/?q=RTX%203090%20Ti&restrict_sr=1&sort=top"])
    assert use_shell is True
    assert '"https://www.reddit.com/r/LocalLLaMA/search/?q=RTX%203090%20Ti&restrict_sr=1&sort=top"' in command


def test_coverage_plan_reports_all_dimensions_and_query_provenance(tmp_path):
    module = load_script("reddit_research.py")
    plan = tmp_path / "coverage.json"
    plan.write_text(json.dumps({"dimensions": [
        {"id": "capacity", "queries": ["VRAM fit"]},
        {"id": "failures", "queries": ["OOM troubleshooting"]},
    ]}), encoding="utf-8")
    args = type("Args", (), {
        "run_id": "coverage-fixture",
        "topic": "coverage fixture",
        "sorts": "relevance",
        "time_filter": "year",
        "subreddit": "LocalLLaMA",
        "coverage_mode": "enabled",
        "coverage_plan": str(plan),
        "target": 50,
        "saturation_window": 5,
        "saturation_min_new": 2,
    })()
    run = module.new_run_manifest(args, ["VRAM fit", "OOM troubleshooting"])
    assert run["coverage"]["uncovered_dimensions"] == ["capacity", "failures"]
    run["query_plan"][0]["status"] = "completed"
    module.update_counts(run)
    assert run["coverage"]["covered_dimensions"] == ["capacity"]
    assert run["coverage"]["uncovered_dimensions"] == ["failures"]
    assert run["coverage"]["complete"] is False
    run["query_plan"][1]["status"] = "completed"
    module.update_counts(run)
    assert run["coverage"]["complete"] is True


def test_coverage_enabled_50_item_run_cannot_complete_on_target_only(tmp_path):
    run = json.loads((FIXTURE / "run.json").read_text(encoding="utf-8"))
    run["target_selected_sources"] = 50
    run["threads"] = [
        {"thread_id": f"fixture-{index}", "canonical_url": f"https://www.reddit.com/r/LocalLLaMA/comments/fixture{index}/item/", "title": f"Fixture item {index}", "selected": True, "status": "captured", "discovered_by_query_ids": ["query-1"], "capture_file": None}
        for index in range(50)
    ]
    run["counts"] = {"queries_total": 1, "queries_completed": 1, "discovered_unique": 50, "selected": 50, "captured": 50, "skipped": 0, "pending": 0, "errors": 0}
    run["coverage"] = {"mode": "enabled", "dimensions": [{"id": "uncovered", "queries": ["missing query"]}], "covered_dimensions": [], "uncovered_dimensions": ["uncovered"], "complete": False}
    (tmp_path / "run.json").write_text(json.dumps(run), encoding="utf-8")
    output = subprocess.run([sys.executable, str(SKILL / "scripts" / "reddit_research.py"), "validate", "--run-dir", str(tmp_path), "--require-target"], capture_output=True, text=True)
    assert output.returncode != 0
    assert "coverage incomplete" in output.stdout
    assert "uncovered" in output.stdout


def test_coverage_enabled_run_cannot_complete_on_target_only(tmp_path):
    module = load_script("reddit_research.py")
    run = json.loads((FIXTURE / "run.json").read_text(encoding="utf-8"))
    run["target_selected_sources"] = 1
    run["coverage"] = {
        "mode": "enabled",
        "dimensions": [{"id": "uncovered", "queries": ["missing query"]}],
        "covered_dimensions": [],
        "uncovered_dimensions": ["uncovered"],
        "complete": False,
    }
    run["query_plan"][0]["status"] = "completed"
    (tmp_path / "run.json").write_text(json.dumps(run), encoding="utf-8")
    result = module.validate(type("Args", (), {"run_dir": str(tmp_path), "require_target": True})())
    assert result != 0
    output = subprocess.run([sys.executable, str(SKILL / "scripts" / "reddit_research.py"), "validate", "--run-dir", str(tmp_path), "--require-target"], capture_output=True, text=True)
    assert "coverage incomplete" in output.stdout
    assert "uncovered" in output.stdout


def test_coverage_plan_rejects_empty_and_unknown_queries(tmp_path):
    module = load_script("reddit_research.py")
    empty = tmp_path / "empty.json"
    empty.write_text(json.dumps({"dimensions": []}), encoding="utf-8")
    with pytest.raises(module.CoveragePlanError):
        module.load_coverage_plan(empty, "enabled", ["known"])
    unknown = tmp_path / "unknown.json"
    unknown.write_text(json.dumps({"dimensions": [{"id": "x", "queries": ["missing"]}]}), encoding="utf-8")
    with pytest.raises(module.CoveragePlanError):
        module.load_coverage_plan(unknown, "enabled", ["known"])


def test_discovery_helpers_are_deterministic():
    module = load_script("reddit_research.py")
    canonical = module.canonical_reddit_url("https://old.reddit.com/r/LocalLLaMA/comments/abc123/title/?utm_source=x#comments")
    assert canonical == "https://www.reddit.com/r/LocalLLaMA/comments/abc123/title/"
    first = module.query_record("LocalLLaMA", "RTX 3090 Ti LLM", "top", "year")
    second = module.query_record("LocalLLaMA", "RTX 3090 Ti LLM", "top", "year")
    assert first["query_id"] == second["query_id"]
    assert first["search_url"] == second["search_url"]


def test_valid_capture_is_ready_and_chrome_is_removed():
    module = load_script("reddit_research.py")
    capture = {
        "canonical_url": "https://www.reddit.com/r/LocalLLaMA/comments/abc123/fixture/",
        "title": "Repost\nGo to LocalLLaMA\nA useful benchmark",
        "post_body": "Repost\nGo to LocalLLaMA\n24GB VRAM\n50 tok/s on llama.cpp",
        "has_post_element": True,
    }
    prepared = module.prepare_capture(capture)
    assert prepared["readiness"] == {"ready": True, "reason": None, "method": "reddit-dom-content-v1"}
    assert "Repost" not in prepared["post_body"]
    assert "Go to LocalLLaMA" not in prepared["post_body"]
    assert "24GB VRAM" in prepared["post_body"]


def test_shell_and_empty_captures_return_stable_not_ready_reasons():
    module = load_script("reddit_research.py")
    base = {"canonical_url": "https://www.reddit.com/r/LocalLLaMA/comments/abc123/fixture/", "has_post_element": True}
    assert module.capture_readiness_reason({**base, "title": "Reddit - The heart of the internet", "post_body": ""}) == "shell-page-title"
    assert module.capture_readiness_reason({**base, "title": "A thread", "post_body": ""}) == "empty-post-body"
    assert module.capture_readiness_reason({**base, "title": "A thread", "post_body": "short"}) == "post-body-too-short"
    assert module.capture_readiness_reason({**base, "title": "A thread", "post_body": "useful post body", "has_post_element": False}) == "missing-post-element"


def test_quality_score_is_deterministic_explainable_and_bounded():
    module = load_script("reddit_research.py")
    capture = {
        "title": "RTX 3090 Ti benchmark",
        "post_body": "24GB VRAM 50 tok/s 64k context 300 watt power limit command --flash-attn",
        "comments": [{"text": "replicated", "author": "a", "score": "3"}] * 10,
        "external_links": ["https://github.com/org/repo"],
    }
    score = module.score_capture(capture, ["rtx 3090 ti", "vram", "context"])
    assert score == module.score_capture(capture, ["rtx 3090 ti", "vram", "context"])
    assert 0 <= score["score"] <= 1
    assert score["scoring_version"] == "evidence-triage-v2"
    assert score["source_type"] == "benchmark"
    assert score["evidence_fields"]["measurements"] is True
    assert score["evidence_fields"]["environment"] is True
    assert score["evidence_fields"]["exact_commands"] is True
    assert score["evidence_fields"]["primary_reference"] is True
    assert score["method"] == "deterministic-source-type-and-evidence-v2"


def test_keywords_alone_cannot_create_high_quality_score():
    module = load_script("reddit_research.py")
    capture = {"title": "RTX 3090 Ti Qwen VRAM context", "post_body": "vram context qwen llama.cpp tokens/s power temperature", "comments": []}
    score = module.score_capture(capture, ["rtx 3090 ti", "vram", "context", "qwen"])
    assert score["evidence_completeness"] < 0.5
    assert score["score"] < 0.6


def test_review_metadata_is_separate_and_serializable():
    module = load_script("reddit_research.py")
    review = module.default_review()
    assert review == {"decision": "unreviewed", "rationale": None, "reviewer": None, "follow_up_status": "not-started"}
    assert set(review) == {"decision", "rationale", "reviewer", "follow_up_status"}


def test_error_sanitizer_redacts_paths_and_secrets():
    module = load_script("reddit_research.py")
    message = "C:/Users/alice/profile cookie=secret Authorization:Bearer abc123 sk-secretvalue /home/alice/private.log api_key=hidden"
    sanitized = module.sanitize_diagnostic(message)
    assert "alice" not in sanitized
    assert "secretvalue" not in sanitized
    assert "hidden" not in sanitized
    assert "<redacted>" in sanitized


def test_receipt_reports_honest_completion_counts(tmp_path):
    script = SKILL / "scripts" / "reddit_research.py"
    output = tmp_path / "receipt.json"
    result = subprocess.run([sys.executable, str(script), "receipt", "--run-dir", str(FIXTURE), "--output", str(output)], capture_output=True, text=True)
    assert result.returncode == 0
    receipt = json.loads(output.read_text(encoding="utf-8"))
    assert receipt["skill_used"] == "reddit-deep-research"
    assert receipt["counts"]["captured"] == 1
    assert receipt["counts"]["errors"] == 0
    assert receipt["complete"] is True


def test_follow_up_ledger_is_not_overwritten_on_resume():
    script_text = (SKILL / "scripts" / "reddit_research.py").read_text(encoding="utf-8")
    assert 'if not follow_up_path.exists()' in script_text


def test_outbound_normalization_filters_and_deduplicates():
    module = load_script("reddit_research.py")
    normalized, reason = module.normalize_outbound_url("https://GitHub.com/org/repo?utm_source=reddit&b=2&a=1#readme")
    assert reason is None
    assert normalized == "https://github.com/org/repo?a=1&b=2"
    assert module.normalize_outbound_url("https://www.reddit.com/r/LocalLLaMA/comments/abc/")[1] == "excluded-domain"
    assert module.score_outbound_url(normalized) == (100, "primary")


def test_outbound_ledger_preserves_provenance_and_priority(tmp_path):
    module = load_script("reddit_research.py")
    run = json.loads((FIXTURE / "run.json").read_text(encoding="utf-8"))
    capture_source = FIXTURE / run["threads"][0]["capture_file"]
    capture = json.loads(capture_source.read_text(encoding="utf-8"))
    capture["outbound_references"] = [
        {"url": "https://github.com/org/repo?utm_source=reddit", "verification_state": "unverified"},
        {"url": "https://github.com/org/repo", "verification_state": "unverified"},
        {"url": "https://www.reddit.com/r/LocalLLaMA/comments/other/", "verification_state": "unverified"},
    ]
    target_capture = tmp_path / run["threads"][0]["capture_file"]
    target_capture.parent.mkdir(parents=True)
    target_capture.write_text(json.dumps(capture), encoding="utf-8")
    ledger = module.build_outbound_ledger(tmp_path, run)
    included = [r for r in ledger["references"] if r["included"]]
    excluded = [r for r in ledger["references"] if not r["included"]]
    assert len(included) == 1
    assert included[0]["source_count"] == 1
    assert included[0]["priority_class"] == "primary"
    assert included[0]["original_urls"] == ["https://github.com/org/repo?utm_source=reddit", "https://github.com/org/repo"]
    assert excluded[0]["filter_reason"] == "excluded-domain"


def test_outbound_ledger_is_separate_from_immutable_capture(tmp_path):
    module = load_script("reddit_research.py")
    run = json.loads((FIXTURE / "run.json").read_text(encoding="utf-8"))
    capture_source = FIXTURE / run["threads"][0]["capture_file"]
    capture_target = tmp_path / run["threads"][0]["capture_file"]
    capture_target.parent.mkdir(parents=True)
    capture_target.write_bytes(capture_source.read_bytes())
    before = capture_target.read_bytes()
    ledger = module.build_outbound_ledger(tmp_path, run)
    module.json_dump(tmp_path / "outbound-references.json", ledger)
    assert capture_target.read_bytes() == before
    assert ledger["references"][0]["verification_state"] == "unverified"
