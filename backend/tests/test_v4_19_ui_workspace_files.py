from pathlib import Path

def test_v419_ui_workspace_files():
    root = Path(__file__).resolve().parents[2]
    app = root / "frontend" / "src" / "App.tsx"
    css = root / "frontend" / "src" / "styles" / "workspace-polish.css"
    assert app.exists()
    assert css.exists()
    text = app.read_text(encoding="utf-8")
    assert "WorkspaceButton" in text
    assert "DeveloperWorkspace" in text
