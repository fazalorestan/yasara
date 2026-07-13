from app.intelligence_v1.domain.models import IndicatorPack, MarketRegime, MarketStructurePack, TrendDirection

class RegimeClassifier:
    def classify(self, indicators: IndicatorPack, structure: MarketStructurePack) -> MarketRegime:
        atr = indicators.atr_14 or 0
        rel_vol = indicators.relative_volume or 0
        if rel_vol >= 2:
            return MarketRegime.HIGH_VOLATILITY
        if rel_vol and rel_vol < 0.55:
            return MarketRegime.LOW_VOLATILITY
        if structure.trend in {TrendDirection.BULLISH, TrendDirection.BEARISH}:
            return MarketRegime.TRENDING
        if structure.trend == TrendDirection.SIDEWAYS:
            return MarketRegime.RANGING
        return MarketRegime.UNKNOWN
