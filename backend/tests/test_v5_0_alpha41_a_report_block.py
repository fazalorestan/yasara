from app.platform_core.strategy_engine.report import StrategyCoreReport

def test_v500_alpha41_a_report_block(): assert StrategyCoreReport().report()['execution_allowed'] is False
