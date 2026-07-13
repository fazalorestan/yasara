from pathlib import Path
def test_trading_account_data_exists():
    root = Path(__file__).resolve().parents[2]
    text = (root / "frontend" / "src" / "data" / "tradingAccount.ts").read_text(encoding="utf-8")
    assert "portfolioMetrics" in text and "positions" in text and "orders" in text and "recentTrades" in text
