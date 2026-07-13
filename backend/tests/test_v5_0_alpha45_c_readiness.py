from app.platform_core.production_runtime.lifecycle_readiness import RuntimeLifecycleReadinessGate

def test_readiness(): assert RuntimeLifecycleReadinessGate().run()['ready'] is True
