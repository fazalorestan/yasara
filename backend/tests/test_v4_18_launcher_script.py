from pathlib import Path

def test_v418_launcher_script():
    root = Path(__file__).resolve().parents[2]
    assert (root / "scripts" / "yasara_one_command_launcher.py").exists()
    text = (root / "scripts" / "yasara_one_command_launcher.py").read_text(encoding="utf-8")
    assert "def start(" in text
    assert "webbrowser.open" in text
