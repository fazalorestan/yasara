from app.platform_core.strategy_engine.strategy_registry import StrategyRegistry

def test_v500_alpha41_a_strategy_get(): assert StrategyRegistry().get('trend.following')['ready'] is True
