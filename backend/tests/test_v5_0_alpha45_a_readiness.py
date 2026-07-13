from app.platform_core.production_runtime.runtime_readiness import RuntimeReadinessGate

def test_readiness(): assert RuntimeReadinessGate().run()['ready'] is True
