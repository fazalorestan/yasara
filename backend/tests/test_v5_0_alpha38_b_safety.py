from app.platform_core.exchange_layer.market_data_safety import ExchangeMarketDataSafetyService

def test_v500_alpha38_b_safety(): assert ExchangeMarketDataSafetyService().policy()['market_data_only'] is True