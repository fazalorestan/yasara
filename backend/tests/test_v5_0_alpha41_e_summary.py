from app.v500_alpha41_strategy_enterprise.models import StrategyEnterpriseSummaryV500Alpha41

def test_v500_alpha41_e_summary():
 s=StrategyEnterpriseSummaryV500Alpha41(); assert s.ready and s.test_pack_size==65
