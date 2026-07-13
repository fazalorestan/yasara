from app.platform_core.production_runtime.enterprise.readiness import RuntimeEnterpriseReadinessGate

def test_readiness(): assert RuntimeEnterpriseReadinessGate().run()['ready'] is True
