from app.v500_alpha32_strategy_optimizer_pro.service import StrategyOptimizerProFacadeV500Alpha32

def test_v500_alpha32_facade_walk_forward():
 r=StrategyOptimizerProFacadeV500Alpha32().walk_forward(); assert r is not None
