from pathlib import Path
def test_trading_terminal_components_exist():
    root = Path(__file__).resolve().parents[2]
    components = root / "frontend" / "src" / "components" / "trading"
    assert (components / "TerminalHeader.tsx").exists()
    assert (components / "TradingChart.tsx").exists()
    assert (components / "TimeframeToolbar.tsx").exists()
    assert (components / "ProfessionalWatchlist.tsx").exists()
    assert (components / "MarketHeat.tsx").exists()
