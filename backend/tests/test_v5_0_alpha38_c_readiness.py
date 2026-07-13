from app.platform_core.exchange_layer.connectivity_readiness import ExchangeConnectivityReadinessGate

def test_v500_alpha38_c_readiness(): assert ExchangeConnectivityReadinessGate().run()['ready'] is True