from app.platform_core.strategy_engine.allocation_safety import StrategyAllocationSafetyPolicy

def test_v500_alpha41_c_safety(): assert StrategyAllocationSafetyPolicy().policy()['broker_connection_enabled'] is False
