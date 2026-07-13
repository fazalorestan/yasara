from app.platform_core.indicators.scanner.watchlist_adapter import IndicatorWatchlistAdapter

def test_v446_watchlist_adapter():
    item = IndicatorWatchlistAdapter().from_bridge_output({"scanner": {"symbol": "BTCUSDT", "direction": "LONG", "score": 72}})
    assert item["symbol"] == "BTCUSDT"
    assert item["execution_allowed"] is False
