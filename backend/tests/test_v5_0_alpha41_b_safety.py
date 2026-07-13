from app.platform_core.strategy_engine.scoring_safety import StrategyScoringSafetyPolicy

def test_v500_alpha41_b_safety(): assert StrategyScoringSafetyPolicy().policy()['scoring_only'] is True
