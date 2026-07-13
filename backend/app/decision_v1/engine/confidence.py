from app.decision_v1.domain.models import ConfidenceBreakdown, DecisionWeights
from app.intelligence_v1.domain.models import MarketIntelligenceReport, TrendDirection, MarketRegime

class ConfidenceEngineV1:
    def calculate(self, report: MarketIntelligenceReport) -> ConfidenceBreakdown:
        tfs = list(report.timeframes.values())
        if not tfs:
            return ConfidenceBreakdown()

        trend = 70 if report.overall_trend in {TrendDirection.BULLISH, TrendDirection.BEARISH} else 35
        regime = 70 if report.overall_regime == MarketRegime.TRENDING else 55 if report.overall_regime == MarketRegime.RANGING else 45

        rsi_scores = []
        macd_scores = []
        structure_scores = []
        volume_scores = []
        volatility_scores = []
        aligned = 0

        for tf in tfs:
            if tf.structure.trend == report.overall_trend:
                aligned += 1
            rsi = tf.indicators.rsi_14
            if rsi is None:
                rsi_scores.append(40)
            elif 45 <= rsi <= 65:
                rsi_scores.append(75)
            elif 30 <= rsi < 45 or 65 < rsi <= 75:
                rsi_scores.append(60)
            else:
                rsi_scores.append(35)

            hist = tf.indicators.macd_histogram
            if hist is None:
                macd_scores.append(40)
            elif (report.overall_trend == TrendDirection.BULLISH and hist > 0) or (report.overall_trend == TrendDirection.BEARISH and hist < 0):
                macd_scores.append(75)
            else:
                macd_scores.append(45)

            structure_scores.append(tf.scores.confidence)
            rel_vol = tf.indicators.relative_volume
            volume_scores.append(75 if rel_vol and rel_vol >= 1.2 else 55 if rel_vol else 40)
            atr = tf.indicators.atr_14
            volatility_scores.append(65 if atr else 40)

        n = max(1, len(tfs))
        return ConfidenceBreakdown(
            trend=trend,
            rsi=sum(rsi_scores) / n,
            macd=sum(macd_scores) / n,
            structure=sum(structure_scores) / n,
            volume=sum(volume_scores) / n,
            volatility=sum(volatility_scores) / n,
            multi_timeframe=aligned / n * 100,
            regime=regime,
        )

    def weighted_score(self, breakdown: ConfidenceBreakdown, weights: DecisionWeights | None = None) -> float:
        w = (weights or DecisionWeights()).normalized()
        data = breakdown.model_dump()
        score = sum(data.get(k, 0) * weight for k, weight in w.items())
        return max(0, min(100, score))
