import importlib.util
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / ".agents" / "skills" / "reddit-deep-research" / "scripts" / "sanitize_artifacts.py"
FIXTURE = ROOT / "tests" / "fixtures" / "reddit-sanitizer" / "mixed.txt"


def load_module():
    spec = importlib.util.spec_from_file_location("sanitize_artifacts", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_sanitize_text_replaces_supported_categories_and_preserves_public_text():
    module = load_module()
    source = FIXTURE.read_text(encoding="utf-8")
    sanitized, counts = module.sanitize_text(source)
    assert "C:\\Users\\alice" not in sanitized
    assert "/home/alice" not in sanitized
    assert "192.168.1.111" not in sanitized
    assert "super-secret-value" not in sanitized
    assert "eyJhbGciOiJfake" not in sanitized
    assert "sk-abcdefghijklmnop" not in sanitized
    assert "https://github.com/org/repo?x=1" in sanitized
    assert "192.0.2.10" in sanitized
    assert "/research/notes" in sanitized
    assert counts["windows-path"] == 1
    assert counts["unix-path"] == 1
    assert counts["private-endpoint"] == 1
    assert counts["api-key"] == 1
    assert counts["bearer-token"] == 1
    assert counts["openai-key"] == 1


def test_sanitize_is_idempotent():
    module = load_module()
    first, _ = module.sanitize_text(FIXTURE.read_text(encoding="utf-8"))
    second, counts = module.sanitize_text(first)
    assert first == second
    assert counts == {}


def test_audit_cli_reports_counts_without_raw_matches(tmp_path):
    result = subprocess.run([sys.executable, str(SCRIPT), "audit", "--input", str(FIXTURE)], capture_output=True, text=True, check=True)
    report = json.loads(result.stdout)
    assert report["mode"] == "audit"
    assert report["file_count"] == 1
    assert report["category_counts"]["windows-path"] == 1
    assert "alice" not in result.stdout
    assert "192.168.1.111" not in result.stdout
    assert "super-secret-value" not in result.stdout
    assert "tests/fixtures/reddit-sanitizer/mixed.txt" not in result.stdout
    assert '"path": "mixed.txt"' in result.stdout


def test_sanitize_cli_writes_copy_and_never_changes_source(tmp_path):
    output = tmp_path / "sanitized"
    before = FIXTURE.read_bytes()
    result = subprocess.run([sys.executable, str(SCRIPT), "sanitize", "--input", str(FIXTURE), "--output", str(output)], capture_output=True, text=True, check=True)
    report = json.loads(result.stdout)
    assert report["mode"] == "sanitize"
    assert report["input"] == "<input>"
    assert report["output"] == "<output>"
    assert output.read_text(encoding="utf-8") == load_module().sanitize_text(FIXTURE.read_text(encoding="utf-8"))[0]
    assert FIXTURE.read_bytes() == before


def test_sanitize_rejects_same_input_and_output():
    result = subprocess.run([sys.executable, str(SCRIPT), "sanitize", "--input", str(FIXTURE), "--output", str(FIXTURE)], capture_output=True, text=True)
    assert result.returncode == 2
    assert "different" in result.stderr
