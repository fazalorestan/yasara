from app.platform_core.strategy_engine.signal_evaluator import StrategySignalEvaluator

def test_v500_alpha41_b_signal(): assert StrategySignalEvaluator().evaluate()['side']=='hold'
