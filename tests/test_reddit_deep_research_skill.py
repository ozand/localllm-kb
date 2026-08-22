import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

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


def test_quality_score_is_deterministic_and_bounded():
    module = load_script("reddit_research.py")
    capture = {"title": "RTX 3090 Ti benchmark", "post_body": "24GB VRAM 50 tok/s 64k context 300 watt power limit command --flash-attn", "comments": [{"text": "replicated", "author": "a", "score": "3"}] * 10}
    score = module.score_capture(capture, ["rtx 3090 ti", "vram", "context"])
    assert score == module.score_capture(capture, ["rtx 3090 ti", "vram", "context"])
    assert 0 <= score["score"] <= 1
    assert score["method"] == "deterministic-keyword-v1"


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
