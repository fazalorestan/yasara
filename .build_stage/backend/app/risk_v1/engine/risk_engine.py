from app.decision_v1.domain.models import DecisionDirection
from app.risk_v1.domain.models import (
    AccountSnapshot,
    ExistingExposure,
    RiskAssessment,
    RiskDecision,
    RiskLimits,
    RiskProfile,
)
from app.risk_v1.engine.position_sizing import PositionSizingEngineV1
from app.risk_v1.engine.profiles import RiskProfileFactory
from app.risk_v1.engine.risk_reward import RiskRewardEngineV1
from app.risk_v1.engine.risk_rules import RiskRulesEngineV1

class RiskIntelligenceEngineV1:
    def __init__(self):
        self.profile_factory = RiskProfileFactory()
        self.rr = RiskRewardEngineV1()
        self.rules = RiskRulesEngineV1()
        self.sizing = PositionSizingEngineV1()

    def assess(
        self,
        decision,
        account: AccountSnapshot,
        profile: RiskProfile = RiskProfile.BALANCED,
        existing_exposure: list[ExistingExposure] | None = None,
        limits: RiskLimits | None = None,
    ) -> RiskAssessment:
        risk_limits = limits or self.profile_factory.limits(profile)
        existing = existing_exposure or []
        rr = self.rr.validate(decision.direction, decision.signal, risk_limits.min_risk_reward)
        rule_results = self.rules.evaluate(account, risk_limits, decision.symbol, decision.direction, existing)
        critical_failed = [r.reason for r in rule_results if not r.passed and r.adjustment_factor == 0]
        warnings = [r.reason for r in rule_results if not r.passed and r.adjustment_factor > 0]
        adjustment_factor = 1.0
        for rule in rule_results:
            adjustment_factor *= rule.adjustment_factor

        if decision.direction not in {DecisionDirection.LONG, DecisionDirection.SHORT}:
            critical_failed.append("Decision is not directional.")
        if not rr.valid and decision.direction in {DecisionDirection.LONG, DecisionDirection.SHORT}:
            warnings.append(rr.reason)
            adjustment_factor *= 0.6

        position = self.sizing.confidence_adjusted(account, decision, risk_limits, adjustment_factor)
        adjusted_confidence = max(0, min(100, decision.scores.confidence * adjustment_factor))
        adjusted_probability = max(0, min(100, decision.scores.probability * adjustment_factor))

        if critical_failed:
            risk_decision = RiskDecision.REJECTED
        elif adjustment_factor < 0.85 or warnings:
            risk_decision = RiskDecision.REDUCED
        else:
            risk_decision = RiskDecision.APPROVED

        final_score = adjusted_confidence * 0.35 + adjusted_probability * 0.20 + decision.scores.quality * 0.15 + decision.scores.reliability * 0.15 + (100 if rr.valid else 40) * 0.15

        return RiskAssessment(
            symbol=decision.symbol,
            risk_decision=risk_decision,
            approved=risk_decision != RiskDecision.REJECTED,
            original_decision=decision,
            adjusted_confidence=adjusted_confidence,
            adjusted_probability=adjusted_probability,
            position_size=position,
            risk_reward=rr,
            rules=rule_results,
            warnings=warnings,
            rejection_reasons=critical_failed,
            final_risk_score=max(0, min(100, final_score)),
        )
