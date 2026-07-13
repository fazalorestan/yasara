from pathlib import Path
def test_react_frontend_files_exist():
    root = Path(__file__).resolve().parents[2]
    assert (root / "frontend" / "package.json").exists()
    assert (root / "frontend" / "src" / "App.tsx").exists()
    assert (root / "frontend" / "src" / "main.tsx").exists()
    assert (root / "frontend" / "vite.config.ts").exists()
