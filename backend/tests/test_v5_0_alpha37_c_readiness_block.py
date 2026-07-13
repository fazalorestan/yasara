from app.platform_core.broker_layer.connectivity_readiness import BrokerConnectivityReadinessGate

def test_v500_alpha37_c_readiness_block(): assert BrokerConnectivityReadinessGate().run()['execution_allowed'] is False