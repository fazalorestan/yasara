from app.v500_alpha32_strategy_optimizer_pro.service import StrategyOptimizerProFacadeV500Alpha32

def test_v500_alpha32_facade_monte_carlo():
 r=StrategyOptimizerProFacadeV500Alpha32().monte_carlo(); assert r is not None
