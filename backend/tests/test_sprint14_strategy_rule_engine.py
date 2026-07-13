from app.strategy_builder_v1.domain.models import RuleOperand, RuleOperator, RuleValueSource, StrategyEvaluationContext, StrategyRule
from app.strategy_builder_v1.engine.rule_engine import StrategyRuleEngineV1

def test_rule_engine_indicator_gt_constant():
    rule = StrategyRule(
        rule_id="r1",
        left=RuleOperand(source=RuleValueSource.INDICATOR, key="rsi"),
        operator=RuleOperator.GT,
        right=RuleOperand(source=RuleValueSource.CONSTANT, key="constant", value=50),
    )
    result = StrategyRuleEngineV1().evaluate_rule(rule, StrategyEvaluationContext(symbol="BTC/USDT", indicators={"rsi": 60}))
    assert result.passed is True
