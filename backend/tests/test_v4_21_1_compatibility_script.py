from pathlib import Path

def test_v4211_compatibility_script():
    root = Path(__file__).resolve().parents[2]
    path = root / "scripts" / "apply_v4_21_1_frontend_compatibility.py"
    assert path.exists()
    text = path.read_text(encoding="utf-8")
    assert "WorkspaceButton" in text
    assert "AI Signals" in text
