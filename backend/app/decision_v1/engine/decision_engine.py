from collections import Counter
from app.decision_v1.domain.models import (
    ConfidenceBreakdown,
    DecisionClass,
    DecisionDirection,
    DecisionObject,
    DecisionScores,
    DecisionWeights,
    RuleStatus,
)
from app.decision_v1.engine.confidence import ConfidenceEngineV1
from app.decision_v1.engine.explainability import DecisionExplainabilityEngineV1
from app.decision_v1.engine.rules import RuleEngineV1
from app.decision_v1.engine.signal_plan import SignalPlanBuilderV1
from app.decision_v1.engine.strategies import StrategyEngineV1
from app.intelligence_v1.domain.models import MarketIntelligenceReport

class DecisionEngineV1:
    def __init__(self, weights: DecisionWeights | None = None):
        self.weights = weights or DecisionWeights()
        self.confidence = ConfidenceEngineV1()
        self.rules = RuleEngineV1()
        self.strategies = StrategyEngineV1()
        self.plan = SignalPlanBuilderV1()
        self.explainability = DecisionExplainabilityEngineV1()

    def decide(self, report: MarketIntelligenceReport) -> DecisionObject:
        breakdown = self.confidence.calculate(report)
        base_confidence = self.confidence.weighted_score(breakdown, self.weights)
        rule_results = self.rules.evaluate(report)
        adjusted_confidence = max(0, min(100, base_confidence + self.rules.total_adjustment(rule_results)))
        strategy_results = self.strategies.evaluate(report)
        direction = self._direction(adjusted_confidence, rule_results, strategy_results)
        decision_class = self._classify(direction, adjusted_confidence)
        signal = self.plan.build(report, direction)
        scores = self._scores(report, adjusted_confidence, direction)
        explanation = self.explainability.explain(report, direction, adjusted_confidence, rule_results, strategy_results)
        rank_score = scores.confidence * 0.45 + scores.quality * 0.20 + scores.reliability * 0.20 + scores.reward * 0.15
        return DecisionObject(
            exchange=report.exchange,
            symbol=report.symbol,
            direction=direction,
            decision_class=decision_class,
            scores=scores,
            confidence_breakdown=breakdown,
            weights=self.weights,
            signal=signal,
            rules=rule_results,
            strategies=strategy_results,
            explanation=explanation,
            rank_score=rank_score,
            source={"market_intelligence_generated_at": report.generated_at.isoformat()},
        )

    def _direction(self, confidence: float, rules, strategies) -> DecisionDirection:
        if any(r.status == RuleStatus.FAILED and r.score_adjustment <= -20 for r in rules):
            return DecisionDirection.NO_TRADE
        if confidence < 45:
            return DecisionDirection.NO_TRADE
        if confidence < 58:
            return DecisionDirection.WAIT
        directional = [s.direction for s in strategies if s.direction in {DecisionDirection.LONG, DecisionDirection.SHORT}]
        if not directional:
            return DecisionDirection.WAIT
        return Counter(directional).most_common(1)[0][0]

    def _classify(self, direction: DecisionDirection, confidence: float) -> DecisionClass:
        if direction == DecisionDirection.NO_TRADE:
            return DecisionClass.NO_TRADE
        if direction == DecisionDirection.WAIT:
            return DecisionClass.NEUTRAL
        if direction == DecisionDirection.LONG:
            if confidence >= 85:
                return DecisionClass.STRONG_BUY
            if confidence >= 70:
                return DecisionClass.BUY
            return DecisionClass.WEAK_BUY
        if confidence >= 85:
            return DecisionClass.STRONG_SELL
        if confidence >= 70:
            return DecisionClass.SELL
        return DecisionClass.WEAK_SELL

    def _scores(self, report: MarketIntelligenceReport, confidence: float, direction: DecisionDirection) -> DecisionScores:
        quality = report.quality
        reliability = report.reliability
        risk = 50 if direction in {DecisionDirection.LONG, DecisionDirection.SHORT} else 80
        reward = min(100, confidence * 0.85) if direction in {DecisionDirection.LONG, DecisionDirection.SHORT} else 20
        probability = confidence * 0.65 + reliability * 0.20 + quality * 0.15
        return DecisionScores(
            confidence=max(0, min(100, confidence)),
            probability=max(0, min(100, probability)),
            quality=max(0, min(100, quality)),
            reliability=max(0, min(100, reliability)),
            risk=max(0, min(100, risk)),
            reward=max(0, min(100, reward)),
        )
