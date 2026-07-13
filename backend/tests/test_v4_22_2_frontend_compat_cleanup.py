from pathlib import Path

def test_v4222_frontend_compat_cleanup_script():
    root = Path(__file__).resolve().parents[2]
    script = root / "scripts" / "fix_v4_22_2_frontend_compat_cleanup.py"
    assert script.exists()
    text = script.read_text(encoding="utf-8")
    assert "WorkspaceButton" in text
    assert "DeveloperWorkspace" in text
    assert "AI Signals" in text
    assert "re.sub" in text
