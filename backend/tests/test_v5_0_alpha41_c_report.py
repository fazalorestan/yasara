from app.platform_core.strategy_engine.allocation_report import StrategyAllocationReport

def test_v500_alpha41_c_report(): assert StrategyAllocationReport().report()['ready'] is True
