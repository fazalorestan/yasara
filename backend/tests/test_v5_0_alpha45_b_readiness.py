from app.platform_core.production_runtime.service_readiness import RuntimeServiceReadinessGate

def test_readiness(): assert RuntimeServiceReadinessGate().run()['ready'] is True
