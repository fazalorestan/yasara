from app.v500_alpha41_strategy_simulation.models import StrategySimulationSummaryV500Alpha41

def test_v500_alpha41_d_summary():
 s=StrategySimulationSummaryV500Alpha41(); assert s.ready and s.test_pack_size==60
