from app.platform_core.exchange_layer.readiness import ExchangeLayerCoreReadinessGate

def test_v500_alpha38_a_readiness_block(): assert ExchangeLayerCoreReadinessGate().run()['execution_allowed'] is False
