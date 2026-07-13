from app.platform_core.strategy_engine.strategy_registry import StrategyRegistry

def test_v500_alpha41_a_strategies(): assert StrategyRegistry().list_strategies()['count']==2
