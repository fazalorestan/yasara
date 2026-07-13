from app.platform_core.broker_layer.connectivity_readiness import BrokerConnectivityReadinessGate

def test_v500_alpha37_c_readiness(): assert BrokerConnectivityReadinessGate().run()['ready'] is True