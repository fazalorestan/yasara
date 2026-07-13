from app.platform_core.broker_layer.enterprise.security import BrokerEnterpriseSecurityGate

def test_v500_alpha37_d_security_block(): assert BrokerEnterpriseSecurityGate().evaluate()['execution_allowed'] is False