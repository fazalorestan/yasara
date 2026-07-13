from pathlib import Path
def test_portfolio_orders_components_exist():
    root = Path(__file__).resolve().parents[2]
    components = root / "frontend" / "src" / "components" / "trading"
    for name in ["PortfolioSummary.tsx","PositionsTable.tsx","OrdersTable.tsx","OrderBook.tsx","RecentTrades.tsx","OrderPanel.tsx","FloatingNotifications.tsx"]:
        assert (components / name).exists()
