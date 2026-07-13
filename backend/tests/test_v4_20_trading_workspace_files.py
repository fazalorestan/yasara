from pathlib import Path

def test_v420_trading_workspace_files():
    root = Path(__file__).resolve().parents[2]
    app = root / "frontend" / "src" / "App.tsx"
    css = root / "frontend" / "src" / "styles" / "pro-trading-workspace.css"
    assert app.exists()
    assert css.exists()
    text = app.read_text(encoding="utf-8")
    assert "ptw-terminal-grid" in text
    assert "BottomTabs" in text
    assert "AI Decision" in text
