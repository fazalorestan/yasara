from app.platform_core.strategy_engine.simulation_engine import StrategySimulationEngine

def test_v500_alpha41_d_simulate(): assert StrategySimulationEngine().simulate()['mode']=='simulation_only'
