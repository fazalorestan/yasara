from app.platform_core.strategy_engine.allocation_readiness import StrategyAllocationReadinessGate

def test_v500_alpha41_c_readiness_block(): assert StrategyAllocationReadinessGate().run()['execution_allowed'] is False
