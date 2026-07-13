from app.platform_core.strategy_engine.scoring_report import StrategyScoringReport

def test_v500_alpha41_b_report_block(): assert StrategyScoringReport().report()['execution_allowed'] is False
