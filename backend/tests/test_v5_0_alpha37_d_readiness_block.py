from app.platform_core.broker_layer.enterprise.readiness import BrokerEnterpriseReadinessGate

def test_v500_alpha37_d_readiness_block(): assert BrokerEnterpriseReadinessGate().run()['execution_allowed'] is False
