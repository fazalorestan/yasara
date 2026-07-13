from app.platform_core.exchange_layer.market_data_readiness import ExchangeMarketDataReadinessGate

def test_v500_alpha38_b_readiness_block(): assert ExchangeMarketDataReadinessGate().run()['execution_allowed'] is False