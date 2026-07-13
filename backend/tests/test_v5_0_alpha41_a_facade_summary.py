from app.v500_alpha41_strategy_core.service import StrategyCoreFacadeV500Alpha41

def test_v500_alpha41_a_facade_summary():
 r=StrategyCoreFacadeV500Alpha41().summary(); assert r is not None
