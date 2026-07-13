from app.platform_core.exchange_layer.service import ExchangeLayerCoreService

def test_v500_alpha38_a_service_market_types():
 r=ExchangeLayerCoreService().market_types(); assert r is not None
