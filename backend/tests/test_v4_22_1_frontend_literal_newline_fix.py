from pathlib import Path

def test_v4221_frontend_literal_newline_fix_script():
    root = Path(__file__).resolve().parents[2]
    script = root / "scripts" / "fix_v4_22_frontend_literal_newlines.py"
    assert script.exists()
    text = script.read_text(encoding="utf-8")
    assert "replace" in text
    assert "DeveloperWorkspace" in text
    assert "WorkspaceButton" in text
    assert "AI Signals" in text
