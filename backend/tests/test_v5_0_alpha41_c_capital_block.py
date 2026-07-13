from app.platform_core.strategy_engine.allocation_safety import StrategyAllocationSafetyPolicy

def test_v500_alpha41_c_capital_block(): assert StrategyAllocationSafetyPolicy().can_allocate_real_capital()['allowed'] is False
