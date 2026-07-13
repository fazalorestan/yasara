from app.platform_core.strategy_engine.simulation_safety import StrategySimulationSafetyPolicy

def test_v500_alpha41_d_real_order_block(): assert StrategySimulationSafetyPolicy().can_execute_real_order()['allowed'] is False
