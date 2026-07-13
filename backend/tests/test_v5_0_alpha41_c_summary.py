from app.v500_alpha41_strategy_allocation.models import StrategyAllocationSummaryV500Alpha41

def test_v500_alpha41_c_summary():
 s=StrategyAllocationSummaryV500Alpha41(); assert s.ready and s.test_pack_size==60
