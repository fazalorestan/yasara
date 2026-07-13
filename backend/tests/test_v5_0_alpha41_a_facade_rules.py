from app.v500_alpha41_strategy_core.service import StrategyCoreFacadeV500Alpha41

def test_v500_alpha41_a_facade_rules():
 r=StrategyCoreFacadeV500Alpha41().rules(); assert r is not None
