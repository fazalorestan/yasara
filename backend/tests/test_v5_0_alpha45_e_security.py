from app.platform_core.production_runtime.enterprise.security import RuntimeEnterpriseSecurityGate

def test_security(): assert RuntimeEnterpriseSecurityGate().evaluate()['score'] >= 9.5
