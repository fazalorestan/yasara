from pathlib import Path

def test_v418_frontend_files():
    root = Path(__file__).resolve().parents[2]
    assert (root / "frontend" / "src" / "components" / "operational" / "LauncherStatus.tsx").exists()
    assert (root / "frontend" / "src" / "styles" / "launcher.css").exists()
