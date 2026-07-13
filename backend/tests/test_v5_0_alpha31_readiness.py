from app.platform_core.optimizer.readiness import OptimizerReadinessGate

def test_v500_alpha31_readiness(): assert OptimizerReadinessGate().run()['ready'] is True
