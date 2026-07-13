from app.v500_alpha41_strategy_simulation.service import StrategySimulationFacadeV500Alpha41

def test_v500_alpha41_d_facade_readiness():
 r=StrategySimulationFacadeV500Alpha41().readiness(); assert r is not None
