from app.platform_core.strategy_engine.allocation_report import StrategyAllocationReport

def test_v500_alpha41_c_report_block(): assert StrategyAllocationReport().report()['execution_allowed'] is False
