from app.platform_core.optimizer_pro.service import StrategyOptimizerProService

def test_v500_alpha32_service_multi_objective():
 r=StrategyOptimizerProService().multi_objective(); assert r is not None
