from app.platform_core.broker_layer.broker_readiness import BrokerCoreReadinessGate

def test_v500_alpha43_a_readiness(): assert BrokerCoreReadinessGate().run()['ready'] is True
