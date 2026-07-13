from app.platform_core.market_data.service import MarketDataFoundationService
def test_v500_alpha15_service_symbols():
    assert MarketDataFoundationService().symbols()["ready"] is True
