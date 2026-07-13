from app.strategy_builder_v1.engine.evaluator import StrategyEvaluatorV1
from app.strategy_builder_v1.domain.models import StrategyEvaluationContext
from app.strategy_builder_v1.samples import build_sample_rsi_strategy

def test_strategy_evaluator_entry_passed():
    strategy = build_sample_rsi_strategy()
    context = StrategyEvaluationContext(symbol="BTC/USDT", indicators={"rsi": 61})
    result = StrategyEvaluatorV1().evaluate(strategy, context)
    assert result.entry_passed is True
    assert result.confidence == 100
