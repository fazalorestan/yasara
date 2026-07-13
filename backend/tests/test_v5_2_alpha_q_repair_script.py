from pathlib import Path

def test_projectwide_repair_script_exists():
    root = Path(__file__).resolve().parents[2]
    text = (root / "scripts/repair_literal_newlines_projectwide.py").read_text(encoding="utf-8")
    assert "backend/app" in text
    assert 'replace("\\\\n", "\\n")' in text or "replace" in text
