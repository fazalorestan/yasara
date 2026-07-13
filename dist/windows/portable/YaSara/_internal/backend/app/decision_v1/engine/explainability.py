from app.decision_v1.domain.models import DecisionDirection, DecisionExplanation, RuleResult, RuleStatus, StrategyResult
from app.intelligence_v1.domain.models import MarketIntelligenceReport

class DecisionExplainabilityEngineV1:
    def explain(self, report: MarketIntelligenceReport, direction: DecisionDirection, confidence: float, rules: list[RuleResult], strategies: list[StrategyResult]) -> DecisionExplanation:
        confirmations = []
        warnings = []
        failed = []

        for rule in rules:
            if rule.status == RuleStatus.PASSED:
                confirmations.append(rule.reason)
            elif rule.status == RuleStatus.WARNING:
                warnings.append(rule.reason)
            elif rule.status == RuleStatus.FAILED:
                failed.append(rule.reason)

        strategy_reasons = []
        for strategy in strategies:
            if strategy.direction == direction:
                strategy_reasons.extend(strategy.reasons)

        if direction == DecisionDirection.NO_TRADE:
            summary = "No Trade because confidence/rules are insufficient."
        elif direction == DecisionDirection.WAIT:
            summary = "Wait because the market does not provide a high-quality directional edge."
        else:
            summary = f"{direction.value.upper()} decision generated with {confidence:.2f}% confidence."

        reasons = [
            f"Overall trend: {report.overall_trend.value}.",
            f"Overall regime: {report.overall_regime.value}.",
            f"Report quality: {report.quality:.2f}.",
            *strategy_reasons[:8],
        ]
        return DecisionExplanation(
            summary=summary,
            reasons=reasons,
            confirmations=confirmations,
            warnings=warnings,
            failed_rules=failed,
        )
