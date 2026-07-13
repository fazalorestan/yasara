from app.platform_core.strategy_engine.simulation_safety import StrategySimulationSafetyPolicy

def test_v500_alpha41_d_safety(): assert StrategySimulationSafetyPolicy().policy()['simulation_only'] is True
