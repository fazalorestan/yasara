from app.v500_alpha41_strategy_allocation.service import StrategyAllocationFacadeV500Alpha41

def test_v500_alpha41_c_facade_safety():
 r=StrategyAllocationFacadeV500Alpha41().safety(); assert r is not None
