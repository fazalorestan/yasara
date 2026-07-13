from app.platform_core.strategy_engine.scoring_report import StrategyScoringReport

def test_v500_alpha41_b_report(): assert StrategyScoringReport().report()['ready'] is True
