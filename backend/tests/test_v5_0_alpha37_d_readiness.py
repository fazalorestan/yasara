from app.platform_core.broker_layer.enterprise.readiness import BrokerEnterpriseReadinessGate

def test_v500_alpha37_d_readiness(): assert BrokerEnterpriseReadinessGate().run()['ready'] is True
