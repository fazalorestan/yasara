from app.strategy_builder_v1.domain.models import RuleOperand, RuleValueSource, StrategyEvaluationContext

class StrategyValueResolverV1:
    def resolve(self, operand: RuleOperand, context: StrategyEvaluationContext, previous: bool = False):
        if operand.source == RuleValueSource.CONSTANT:
            return operand.value
        if operand.source == RuleValueSource.INDICATOR:
            return (context.previous_indicators if previous else context.indicators).get(operand.key)
        if operand.source == RuleValueSource.MARKET_FIELD:
            return (context.previous_market_fields if previous else context.market_fields).get(operand.key)
        if operand.source == RuleValueSource.ANALYSIS_FIELD:
            return context.analysis_fields.get(operand.key)
        return None
