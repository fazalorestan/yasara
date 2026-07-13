from app.platform_core.market_data.snapshot_service import MarketDataSnapshotService
def test_v500_alpha15_snapshot_samples():
    s = MarketDataSnapshotService()
    assert s.sample_ohlcv()["symbol"] == "BTCUSDT"
    assert len(s.sample_orderbook()["bids"]) == 2
