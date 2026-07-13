from app.platform_core.optimizer_pro.service import StrategyOptimizerProService

def test_v500_alpha32_service_walk_forward():
 r=StrategyOptimizerProService().walk_forward(); assert r is not None
