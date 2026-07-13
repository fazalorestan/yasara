from app.platform_core.optimizer.readiness import OptimizerReadinessGate

def test_v500_alpha31_readiness_blocked(): assert OptimizerReadinessGate().run()['execution_allowed'] is False
