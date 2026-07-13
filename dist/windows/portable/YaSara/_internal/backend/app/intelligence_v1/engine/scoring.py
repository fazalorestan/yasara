from app.intelligence_v1.domain.models import IndicatorPack, MarketRegime, MarketStructurePack, ScoreSet, TrendDirection

class IntelligenceScoringEngine:
    def score(self, candles_count: int, indicators: IndicatorPack, structure: MarketStructurePack, regime: MarketRegime) -> ScoreSet:
        available = sum(value is not None for value in [
            indicators.sma_20,
            indicators.sma_50,
            indicators.ema_20,
            indicators.rsi_14,
            indicators.macd,
            indicators.atr_14,
            indicators.relative_volume,
        ])
        confidence = available / 7 * 55
        if structure.trend in {TrendDirection.BULLISH, TrendDirection.BEARISH}:
            confidence += 20
        if structure.break_of_structure:
            confidence += 10
        if regime != MarketRegime.UNKNOWN:
            confidence += 10

        quality = min(100, candles_count / 250 * 100)
        reliability = 80 if candles_count >= 200 else 65 if candles_count >= 100 else 45
        return ScoreSet(
            confidence=max(0, min(100, confidence)),
            quality=max(0, min(100, quality)),
            reliability=reliability,
        )
