from app.v11_strategy_runtime.models import StrategyActionV11, StrategyConditionTypeV11, StrategyConditionV11, StrategyContextV11, StrategyRuleV11
from app.v11_strategy_runtime.rule_engine import StrategyRuleEngineV11

def test_strategy_rule_engine_evaluate():
    rule = StrategyRuleV11(name="buy", action=StrategyActionV11.BUY, conditions=[
        StrategyConditionV11(condition_type=StrategyConditionTypeV11.AI_SCORE_ABOVE, value=0.5)
    ])
    signal = StrategyRuleEngineV11().evaluate([rule], StrategyContextV11(symbol="BTCUSDT", price=100, ai_score=0.8))
    assert signal.action == StrategyActionV11.BUY
