from app.platform_core.strategy_engine.signal_aggregator import StrategySignalAggregator

def test_v500_alpha41_b_aggregate(): assert StrategySignalAggregator().aggregate()['final_side']=='hold'
