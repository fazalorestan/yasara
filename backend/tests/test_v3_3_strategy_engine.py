from app.v33_strategy_builder.engine import StrategyRuleEngineV33
from app.v33_strategy_builder.models import StrategyConditionV33, StrategyRuleV33

def test_v33_engine():
    engine = StrategyRuleEngineV33()
    rule = StrategyRuleV33(rule_id="r1", name="rule", conditions=[StrategyConditionV33(left="ema20", operator="gt", right="ema50")], action="buy")
    result = engine.evaluate_rule(rule, {"ema20": 20, "ema50": 10})
    assert result["matched"] is True
    assert result["action"] == "buy"
