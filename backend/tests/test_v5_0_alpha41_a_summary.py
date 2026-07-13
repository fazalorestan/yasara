from app.v500_alpha41_strategy_core.models import StrategyCoreSummaryV500Alpha41

def test_v500_alpha41_a_summary():
 s=StrategyCoreSummaryV500Alpha41(); assert s.ready and s.test_pack_size==60
