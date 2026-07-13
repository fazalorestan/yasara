from app.platform_core.broker_layer.enterprise.security import BrokerEnterpriseSecurityGate

def test_v500_alpha37_d_security(): assert BrokerEnterpriseSecurityGate().evaluate()['score'] >= 9.5