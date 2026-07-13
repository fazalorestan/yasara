from app.platform_core.optimizer_pro.readiness import StrategyOptimizerProReadinessGate

def test_v500_alpha32_readiness():
 r=StrategyOptimizerProReadinessGate().run(); assert r['ready'] is True and r['execution_allowed'] is False
