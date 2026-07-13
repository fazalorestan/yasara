from app.platform_core.exchange_layer.readiness import ExchangeLayerCoreReadinessGate

def test_v500_alpha38_a_readiness(): assert ExchangeLayerCoreReadinessGate().run()['ready'] is True
