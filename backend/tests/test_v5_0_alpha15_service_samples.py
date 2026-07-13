from app.platform_core.market_data.service import MarketDataFoundationService
def test_v500_alpha15_service_samples():
    r = MarketDataFoundationService().samples("BTCUSDT")
    assert r["ready"] is True
    assert r["execution_allowed"] is False
