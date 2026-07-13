from app.platform_core.broker_layer.enterprise.security import BrokerEnterpriseSecurityGate

def test_v500_alpha37_d_security_checks(): assert BrokerEnterpriseSecurityGate().evaluate()['checks']['real_execution_blocked'] is True