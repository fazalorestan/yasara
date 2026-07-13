from app.v500_alpha41_strategy_simulation.service import StrategySimulationFacadeV500Alpha41

def test_v500_alpha41_d_facade_report():
 r=StrategySimulationFacadeV500Alpha41().report(); assert r is not None
