from app.strategy_builder_v1.domain.models import RuleEvaluationResult, RuleOperator, StrategyRule, StrategyEvaluationContext
from app.strategy_builder_v1.engine.value_resolver import StrategyValueResolverV1

class StrategyRuleEngineV1:
    def __init__(self):
        self.resolver = StrategyValueResolverV1()

    def evaluate_rule(self, rule: StrategyRule, context: StrategyEvaluationContext) -> RuleEvaluationResult:
        left = self.resolver.resolve(rule.left, context)
        right = self.resolver.resolve(rule.right, context)

        if left is None or right is None:
            return RuleEvaluationResult(rule_id=rule.rule_id, passed=False, score=0, message="Missing operand value.")

        passed = self._compare(rule.operator, left, right, rule, context)
        score = rule.weight if passed else 0
        return RuleEvaluationResult(
            rule_id=rule.rule_id,
            passed=passed,
            score=score,
            message="Rule passed." if passed else "Rule failed.",
        )

    def _compare(self, operator: RuleOperator, left, right, rule: StrategyRule, context: StrategyEvaluationContext) -> bool:
        if operator == RuleOperator.GT:
            return left > right
        if operator == RuleOperator.GTE:
            return left >= right
        if operator == RuleOperator.LT:
            return left < right
        if operator == RuleOperator.LTE:
            return left <= right
        if operator == RuleOperator.EQ:
            return left == right
        if operator == RuleOperator.NEQ:
            return left != right
        if operator == RuleOperator.CROSSES_ABOVE:
            prev_left = self.resolver.resolve(rule.left, context, previous=True)
            prev_right = self.resolver.resolve(rule.right, context, previous=True)
            return prev_left is not None and prev_right is not None and prev_left <= prev_right and left > right
        if operator == RuleOperator.CROSSES_BELOW:
            prev_left = self.resolver.resolve(rule.left, context, previous=True)
            prev_right = self.resolver.resolve(rule.right, context, previous=True)
            return prev_left is not None and prev_right is not None and prev_left >= prev_right and left < right
        return False
