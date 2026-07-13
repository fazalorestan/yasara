from app.platform_core.exchange_layer.market_data_safety import ExchangeMarketDataSafetyService

def test_v500_alpha38_b_validate_bad(): assert ExchangeMarketDataSafetyService().validate_symbol('BTC')['valid'] is False