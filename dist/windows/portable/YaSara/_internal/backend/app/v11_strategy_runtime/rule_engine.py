from app.v11_strategy_runtime.models import (
    StrategyActionV11,
    StrategyConditionTypeV11,
    StrategyContextV11,
    StrategyRuleV11,
    StrategySignalV11,
)


class StrategyRuleEngineV11:
    def condition_matches(self, condition, context: StrategyContextV11) -> bool:
        if condition.symbol and condition.symbol.upper() != context.symbol.upper():
            return False
        if condition.condition_type == StrategyConditionTypeV11.PRICE_ABOVE:
            return context.price > float(condition.value)
        if condition.condition_type == StrategyConditionTypeV11.PRICE_BELOW:
            return context.price < float(condition.value)
        if condition.condition_type == StrategyConditionTypeV11.AI_SCORE_ABOVE:
            return context.ai_score > float(condition.value)
        if condition.condition_type == StrategyConditionTypeV11.RISK_ALLOWED:
            return context.risk_allowed is bool(condition.value)
        return False

    def evaluate_rule(self, rule: StrategyRuleV11, context: StrategyContextV11) -> bool:
        if not rule.enabled:
            return False
        return all(self.condition_matches(condition, context) for condition in rule.conditions)

    def evaluate(self, rules: list[StrategyRuleV11], context: StrategyContextV11) -> StrategySignalV11:
        matched = [rule for rule in rules if self.evaluate_rule(rule, context)]
        if not matched:
            return StrategySignalV11(
                symbol=context.symbol.upper(),
                action=StrategyActionV11.HOLD,
                confidence=0.3,
                reason="No strategy rule matched.",
            )
        if not context.risk_allowed:
            return StrategySignalV11(
                symbol=context.symbol.upper(),
                action=StrategyActionV11.BLOCK,
                confidence=1.0,
                matched_rules=[rule.rule_id for rule in matched],
                reason="Risk guard blocked strategy action.",
            )
        selected = matched[0]
        return StrategySignalV11(
            symbol=context.symbol.upper(),
            action=selected.action,
            confidence=min(0.5 + context.ai_score, 1.0),
            matched_rules=[rule.rule_id for rule in matched],
            reason=f"Matched strategy rule: {selected.name}",
        )
