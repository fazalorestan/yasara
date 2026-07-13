from app.platform_core.optimizer_pro.service import StrategyOptimizerProService

def test_v500_alpha32_service_monte_carlo():
 r=StrategyOptimizerProService().monte_carlo(); assert r is not None
