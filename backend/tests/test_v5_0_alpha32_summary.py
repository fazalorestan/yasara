from app.v500_alpha32_strategy_optimizer_pro.models import StrategyOptimizerProSummaryV500Alpha32

def test_v500_alpha32_summary():
 s=StrategyOptimizerProSummaryV500Alpha32(); assert s.ready and s.test_pack_size==50