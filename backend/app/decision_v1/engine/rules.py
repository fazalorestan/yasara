from abc import ABC, abstractmethod
from app.decision_v1.domain.models import RuleResult, RuleStatus
from app.intelligence_v1.domain.models import MarketIntelligenceReport, TrendDirection, MarketRegime

class DecisionRule(ABC):
    name: str
    enabled: bool = True

    @abstractmethod
    def evaluate(self, report: MarketIntelligenceReport) -> RuleResult:
        raise NotImplementedError

class TrendFilterRule(DecisionRule):
    name = "trend_filter"
    def evaluate(self, report: MarketIntelligenceReport) -> RuleResult:
        if not self.enabled:
            return RuleResult(name=self.name, status=RuleStatus.DISABLED)
        if report.overall_trend == TrendDirection.UNKNOWN:
            return RuleResult(name=self.name, status=RuleStatus.FAILED, score_adjustment=-20, reason="Trend is unknown.")
        if report.overall_trend == TrendDirection.SIDEWAYS:
            return RuleResult(name=self.name, status=RuleStatus.WARNING, score_adjustment=-8, reason="Market is sideways.")
        return RuleResult(name=self.name, status=RuleStatus.PASSED, score_adjustment=5, reason="Trend is directional.")

class MultiTimeframeRule(DecisionRule):
    name = "multi_timeframe_alignment"
    def evaluate(self, report: MarketIntelligenceReport) -> RuleResult:
        if not self.enabled:
            return RuleResult(name=self.name, status=RuleStatus.DISABLED)
        if not report.timeframes:
            return RuleResult(name=self.name, status=RuleStatus.FAILED, score_adjustment=-30, reason="No timeframe data.")
        aligned = sum(1 for tf in report.timeframes.values() if tf.structure.trend == report.overall_trend)
        ratio = aligned / max(1, len(report.timeframes))
        if ratio >= 0.67:
            return RuleResult(name=self.name, status=RuleStatus.PASSED, score_adjustment=8, reason="Multi-timeframe trend alignment confirmed.", metadata={"alignment": ratio})
        if ratio >= 0.34:
            return RuleResult(name=self.name, status=RuleStatus.WARNING, score_adjustment=-5, reason="Partial timeframe alignment.", metadata={"alignment": ratio})
        return RuleResult(name=self.name, status=RuleStatus.FAILED, score_adjustment=-18, reason="Weak timeframe alignment.", metadata={"alignment": ratio})

class VolumeFilterRule(DecisionRule):
    name = "volume_filter"
    def evaluate(self, report: MarketIntelligenceReport) -> RuleResult:
        vols = [tf.indicators.relative_volume for tf in report.timeframes.values() if tf.indicators.relative_volume is not None]
        if not vols:
            return RuleResult(name=self.name, status=RuleStatus.WARNING, score_adjustment=-4, reason="Relative volume unavailable.")
        avg = sum(vols) / len(vols)
        if avg >= 1.2:
            return RuleResult(name=self.name, status=RuleStatus.PASSED, score_adjustment=5, reason="Relative volume supports the move.", metadata={"relative_volume": avg})
        if avg < 0.6:
            return RuleResult(name=self.name, status=RuleStatus.WARNING, score_adjustment=-7, reason="Volume is weak.", metadata={"relative_volume": avg})
        return RuleResult(name=self.name, status=RuleStatus.PASSED, score_adjustment=0, reason="Volume is acceptable.", metadata={"relative_volume": avg})

class RegimeFilterRule(DecisionRule):
    name = "regime_filter"
    def evaluate(self, report: MarketIntelligenceReport) -> RuleResult:
        if report.overall_regime == MarketRegime.HIGH_VOLATILITY:
            return RuleResult(name=self.name, status=RuleStatus.WARNING, score_adjustment=-8, reason="High volatility requires reduced confidence.")
        if report.overall_regime == MarketRegime.LOW_VOLATILITY:
            return RuleResult(name=self.name, status=RuleStatus.WARNING, score_adjustment=-6, reason="Low volatility may reduce follow-through.")
        if report.overall_regime in {MarketRegime.TRENDING, MarketRegime.RANGING}:
            return RuleResult(name=self.name, status=RuleStatus.PASSED, score_adjustment=3, reason="Regime is classified.")
        return RuleResult(name=self.name, status=RuleStatus.WARNING, score_adjustment=-4, reason="Regime is unknown.")

class RuleEngineV1:
    def __init__(self):
        self.rules: list[DecisionRule] = [
            TrendFilterRule(),
            MultiTimeframeRule(),
            VolumeFilterRule(),
            RegimeFilterRule(),
        ]

    def evaluate(self, report: MarketIntelligenceReport) -> list[RuleResult]:
        return [rule.evaluate(report) for rule in self.rules]

    def total_adjustment(self, results: list[RuleResult]) -> float:
        return sum(r.score_adjustment for r in results)
