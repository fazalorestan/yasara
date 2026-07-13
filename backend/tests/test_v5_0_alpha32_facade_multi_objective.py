from app.v500_alpha32_strategy_optimizer_pro.service import StrategyOptimizerProFacadeV500Alpha32

def test_v500_alpha32_facade_multi_objective():
 r=StrategyOptimizerProFacadeV500Alpha32().multi_objective(); assert r is not None
