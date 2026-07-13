from app.platform_core.strategy_engine.report import StrategyCoreReport

def test_v500_alpha41_a_report(): assert StrategyCoreReport().report()['ready'] is True
