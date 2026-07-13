from app.strategy_builder_v1.domain.models import RuleGroup, StrategyDefinition, StrategyEvaluationContext, StrategyEvaluationResult
from app.strategy_builder_v1.engine.rule_engine import StrategyRuleEngineV1
from app.strategy_builder_v1.engine.validator import StrategyValidatorV1

class StrategyEvaluatorV1:
    def __init__(self):
        self.rule_engine = StrategyRuleEngineV1()
        self.validator = StrategyValidatorV1()

    def evaluate(self, strategy: StrategyDefinition, context: StrategyEvaluationContext) -> StrategyEvaluationResult:
        validation = self.validator.validate(strategy)
        if not validation.valid:
            return StrategyEvaluationResult(
                strategy_id=strategy.strategy_id,
                name=strategy.name,
                symbol=context.symbol,
                entry_passed=False,
                risk_passed=False,
                score=0,
                confidence=0,
                rejected_rules=[],
            )

        entry_results, entry_passed, entry_score = self._evaluate_group(strategy.entry, context)
        exit_results, exit_passed, exit_score = self._evaluate_group(strategy.exit, context) if strategy.exit else ([], False, 0)
        risk_results, risk_passed, risk_score = self._evaluate_group(strategy.risk_filters, context) if strategy.risk_filters else ([], True, 0)

        all_results = entry_results + exit_results + risk_results
        matched = [r for r in all_results if r.passed]
        rejected = [r for r in all_results if not r.passed]
        total_possible = sum(r.score for r in matched) + sum(self._weight_by_id(strategy, r.rule_id) for r in rejected)
        score = entry_score + exit_score + risk_score
        confidence = (score / total_possible * 100) if total_possible > 0 else 0

        return StrategyEvaluationResult(
            strategy_id=strategy.strategy_id,
            name=strategy.name,
            symbol=context.symbol,
            entry_passed=entry_passed and risk_passed,
            exit_passed=exit_passed,
            risk_passed=risk_passed,
            score=score,
            confidence=max(0, min(100, confidence)),
            matched_rules=matched,
            rejected_rules=rejected,
        )

    def _evaluate_group(self, group: RuleGroup | None, context: StrategyEvaluationContext):
        if group is None:
            return [], True, 0
        results = [self.rule_engine.evaluate_rule(rule, context) for rule in group.rules]
        score = sum(r.score for r in results)
        required_failed = any((not r.passed) and self._required(group, r.rule_id) for r in results)
        passed = score >= group.min_score and not required_failed
        return results, passed, score

    def _required(self, group: RuleGroup, rule_id: str) -> bool:
        for rule in group.rules:
            if rule.rule_id == rule_id:
                return rule.required
        return False

    def _weight_by_id(self, strategy: StrategyDefinition, rule_id: str) -> float:
        for group in [strategy.entry, strategy.exit, strategy.risk_filters]:
            if group:
                for rule in group.rules:
                    if rule.rule_id == rule_id:
                        return rule.weight
        return 0
