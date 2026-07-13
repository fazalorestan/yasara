from app.v500_alpha41_strategy_scoring.models import StrategyScoringSummaryV500Alpha41

def test_v500_alpha41_b_summary():
 s=StrategyScoringSummaryV500Alpha41(); assert s.ready and s.test_pack_size==60
