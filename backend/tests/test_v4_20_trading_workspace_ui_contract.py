from pathlib import Path

def test_v420_trading_workspace_ui_contract():
    root = Path(__file__).resolve().parents[2]
    text = (root / "frontend" / "src" / "App.tsx").read_text(encoding="utf-8")
    for token in ["Watchlist", "Positions", "Orders", "History", "Risk Engine", "Trade Score"]:
        assert token in text
