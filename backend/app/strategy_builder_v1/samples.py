from app.strategy_builder_v1.domain.models import (
    RuleGroup,
    RuleOperand,
    RuleOperator,
    RuleValueSource,
    StrategyDefinition,
    StrategyRule,
)

def build_sample_rsi_strategy() -> StrategyDefinition:
    return StrategyDefinition(
        strategy_id="sample_rsi_long",
        name="Sample RSI Long",
        entry=RuleGroup(
            group_id="entry",
            name="Entry",
            min_score=1,
            rules=[
                StrategyRule(
                    rule_id="rsi_gt_50",
                    left=RuleOperand(source=RuleValueSource.INDICATOR, key="rsi"),
                    operator=RuleOperator.GT,
                    right=RuleOperand(source=RuleValueSource.CONSTANT, key="constant", value=50),
                    weight=1,
                    required=True,
                )
            ],
        ),
    )
