from app.platform_core.optimizer_pro.service import StrategyOptimizerProService

def test_v500_alpha32_service_robustness():
 r=StrategyOptimizerProService().robustness(); assert r is not None
