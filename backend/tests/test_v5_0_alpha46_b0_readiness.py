from app.platform_core.stabilization.stabilization_readiness import StabilizationReadinessGate

def test_readiness(): assert StabilizationReadinessGate().run()['ready'] is True
