from pathlib import Path
def test_market_workspace_components_exist():
    root = Path(__file__).resolve().parents[2]
    components = root / "frontend" / "src" / "components" / "market"
    assert (components / "Watchlist.tsx").exists()
    assert (components / "TopMovers.tsx").exists()
    assert (components / "MarketOverview.tsx").exists()
    assert (components / "SymbolSearch.tsx").exists()
