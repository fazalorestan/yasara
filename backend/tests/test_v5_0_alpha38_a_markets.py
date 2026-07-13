from app.platform_core.exchange_layer.markets import ExchangeMarketTypeService

def test_v500_alpha38_a_markets(): assert 'spot' in ExchangeMarketTypeService().supported_market_types()['market_types']