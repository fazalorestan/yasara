from abc import ABC, abstractmethod
from collections import Counter
from app.decision_v1.domain.models import DecisionDirection, StrategyCode, StrategyResult
from app.intelligence_v1.domain.models import MarketIntelligenceReport, TrendDirection

class DecisionStrategy(ABC):
    code: StrategyCode

    @abstractmethod
    def evaluate(self, report: MarketIntelligenceReport) -> StrategyResult:
        raise NotImplementedError

class TrendStrategy(DecisionStrategy):
    code = StrategyCode.TREND
    def evaluate(self, report: MarketIntelligenceReport) -> StrategyResult:
        if report.overall_trend == TrendDirection.BULLISH:
            return StrategyResult(strategy=self.code, direction=DecisionDirection.LONG, confidence=70, quality=report.quality, reasons=["Overall trend is bullish."])
        if report.overall_trend == TrendDirection.BEARISH:
            return StrategyResult(strategy=self.code, direction=DecisionDirection.SHORT, confidence=70, quality=report.quality, reasons=["Overall trend is bearish."])
        return StrategyResult(strategy=self.code, direction=DecisionDirection.WAIT, confidence=35, quality=report.quality, reasons=["Trend is not directional."])

class BreakoutStrategy(DecisionStrategy):
    code = StrategyCode.BREAKOUT
    def evaluate(self, report: MarketIntelligenceReport) -> StrategyResult:
        latest = list(report.timeframes.values())[-1] if report.timeframes else None
        if not latest or not latest.structure.break_of_structure:
            return StrategyResult(strategy=self.code, direction=DecisionDirection.WAIT, confidence=35, quality=50, reasons=["No break of structure."])
        if latest.structure.trend == TrendDirection.BULLISH:
            return StrategyResult(strategy=self.code, direction=DecisionDirection.LONG, confidence=76, quality=latest.scores.quality, reasons=["Bullish break of structure detected."])
        if latest.structure.trend == TrendDirection.BEARISH:
            return StrategyResult(strategy=self.code, direction=DecisionDirection.SHORT, confidence=76, quality=latest.scores.quality, reasons=["Bearish break of structure detected."])
        return StrategyResult(strategy=self.code, direction=DecisionDirection.WAIT, confidence=45, quality=latest.scores.quality, reasons=["BOS detected but trend unclear."])

class MomentumStrategy(DecisionStrategy):
    code = StrategyCode.MOMENTUM
    def evaluate(self, report: MarketIntelligenceReport) -> StrategyResult:
        scores = []
        for tf in report.timeframes.values():
            hist = tf.indicators.macd_histogram
            rsi = tf.indicators.rsi_14
            if hist is not None and rsi is not None:
                if hist > 0 and 50 <= rsi <= 70:
                    scores.append(1)
                elif hist < 0 and 30 <= rsi <= 50:
                    scores.append(-1)
        if not scores:
            return StrategyResult(strategy=self.code, direction=DecisionDirection.WAIT, confidence=35, quality=50, reasons=["Momentum data incomplete."])
        avg = sum(scores) / len(scores)
        if avg > 0.3:
            return StrategyResult(strategy=self.code, direction=DecisionDirection.LONG, confidence=68, quality=report.quality, reasons=["Momentum favors long."])
        if avg < -0.3:
            return StrategyResult(strategy=self.code, direction=DecisionDirection.SHORT, confidence=68, quality=report.quality, reasons=["Momentum favors short."])
        return StrategyResult(strategy=self.code, direction=DecisionDirection.WAIT, confidence=45, quality=report.quality, reasons=["Momentum is mixed."])

class MeanReversionStrategy(DecisionStrategy):
    code = StrategyCode.MEAN_REVERSION
    def evaluate(self, report: MarketIntelligenceReport) -> StrategyResult:
        latest = list(report.timeframes.values())[-1] if report.timeframes else None
        if not latest or latest.indicators.rsi_14 is None:
            return StrategyResult(strategy=self.code, direction=DecisionDirection.WAIT, confidence=30, quality=50, reasons=["RSI unavailable."])
        rsi = latest.indicators.rsi_14
        if rsi < 28:
            return StrategyResult(strategy=self.code, direction=DecisionDirection.LONG, confidence=58, quality=latest.scores.quality, reasons=["RSI oversold mean-reversion context."])
        if rsi > 72:
            return StrategyResult(strategy=self.code, direction=DecisionDirection.SHORT, confidence=58, quality=latest.scores.quality, reasons=["RSI overbought mean-reversion context."])
        return StrategyResult(strategy=self.code, direction=DecisionDirection.WAIT, confidence=35, quality=latest.scores.quality, reasons=["No mean-reversion edge."])

class CompositeStrategy(DecisionStrategy):
    code = StrategyCode.COMPOSITE
    def __init__(self):
        self.children = [TrendStrategy(), BreakoutStrategy(), MomentumStrategy(), MeanReversionStrategy()]

    def evaluate(self, report: MarketIntelligenceReport) -> StrategyResult:
        results = [s.evaluate(report) for s in self.children]
        directional = [r for r in results if r.direction in {DecisionDirection.LONG, DecisionDirection.SHORT}]
        if not directional:
            return StrategyResult(strategy=self.code, direction=DecisionDirection.WAIT, confidence=35, quality=report.quality, reasons=["No strategy consensus."])
        direction = Counter([r.direction for r in directional]).most_common(1)[0][0]
        selected = [r for r in directional if r.direction == direction]
        confidence = sum(r.confidence for r in selected) / len(selected)
        reasons = [reason for r in selected for reason in r.reasons]
        return StrategyResult(strategy=self.code, direction=direction, confidence=confidence, quality=sum(r.quality for r in selected)/len(selected), reasons=reasons)

class StrategyEngineV1:
    def __init__(self):
        self.strategies = [TrendStrategy(), BreakoutStrategy(), MomentumStrategy(), MeanReversionStrategy(), CompositeStrategy()]

    def evaluate(self, report: MarketIntelligenceReport) -> list[StrategyResult]:
        return [strategy.evaluate(report) for strategy in self.strategies]
