from app.platform_core.production_readiness.readiness import ProductionReadinessGate

def test_readiness(): assert ProductionReadinessGate().run()['ready'] is True
