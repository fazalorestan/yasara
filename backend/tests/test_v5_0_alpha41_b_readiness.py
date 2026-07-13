from app.platform_core.strategy_engine.scoring_readiness import StrategyScoringReadinessGate

def test_v500_alpha41_b_readiness(): assert StrategyScoringReadinessGate().run()['ready'] is True
