from app.platform_core.optimizer_pro.service import StrategyOptimizerProService

def test_v500_alpha32_service_best():
 r=StrategyOptimizerProService().best(); assert r is not None
