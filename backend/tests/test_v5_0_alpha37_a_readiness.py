from app.platform_core.broker_layer.readiness import BrokerLayerCoreReadinessGate

def test_v500_alpha37_a_readiness(): assert BrokerLayerCoreReadinessGate().run()['ready'] is True
