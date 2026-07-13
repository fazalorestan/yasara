from app.platform_core.strategy_engine.strategy_score import StrategyScoreService

def test_v500_alpha41_b_score(): assert StrategyScoreService().score()['grade']=='neutral'
