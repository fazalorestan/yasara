from collections import Counter
from app.intelligence_v1.domain.models import IndicatorPack, MarketIntelligenceReport, MarketRegime, TimeframeIntelligence, TrendDirection
from app.intelligence_v1.engine.indicators import IndicatorCalculator
from app.intelligence_v1.engine.regime import RegimeClassifier
from app.intelligence_v1.engine.scoring import IntelligenceScoringEngine
from app.intelligence_v1.engine.structure import MarketStructureAnalyzer
from app.market_data.domain.models import Candle

class MarketIntelligenceEngineV1:
    def __init__(self):
        self.indicators = IndicatorCalculator()
        self.structure = MarketStructureAnalyzer()
        self.regime = RegimeClassifier()
        self.scoring = IntelligenceScoringEngine()

    def analyze_timeframe(self, symbol: str, timeframe: str, candles: list[Candle]) -> TimeframeIntelligence:
        closes = [c.close for c in candles]
        macd, macd_signal, macd_hist = self.indicators.macd(closes)
        vol_sma, rel_vol = self.indicators.relative_volume(candles)
        pack = IndicatorPack(
            sma_20=self.indicators.sma(closes, 20),
            sma_50=self.indicators.sma(closes, 50),
            ema_20=self.indicators.ema(closes, 20),
            rsi_14=self.indicators.rsi(closes, 14),
            macd=macd,
            macd_signal=macd_signal,
            macd_histogram=macd_hist,
            atr_14=self.indicators.atr(candles, 14),
            volume_sma_20=vol_sma,
            relative_volume=rel_vol,
        )
        structure = self.structure.analyze(candles)
        regime = self.regime.classify(pack, structure)
        scores = self.scoring.score(len(candles), pack, structure, regime)
        return TimeframeIntelligence(
            symbol=symbol,
            timeframe=timeframe,
            candles=len(candles),
            indicators=pack,
            structure=structure,
            regime=regime,
            scores=scores,
        )

    def analyze(self, exchange: str, symbol: str, candles_by_timeframe: dict[str, list[Candle]]) -> MarketIntelligenceReport:
        tf_reports = {
            tf: self.analyze_timeframe(symbol, tf, candles)
            for tf, candles in candles_by_timeframe.items()
            if candles
        }
        trends = [item.structure.trend for item in tf_reports.values() if item.structure.trend != TrendDirection.UNKNOWN]
        regimes = [item.regime for item in tf_reports.values() if item.regime != MarketRegime.UNKNOWN]
        overall_trend = Counter(trends).most_common(1)[0][0] if trends else TrendDirection.UNKNOWN
        overall_regime = Counter(regimes).most_common(1)[0][0] if regimes else MarketRegime.UNKNOWN
        n = max(1, len(tf_reports))
        return MarketIntelligenceReport(
            exchange=exchange,
            symbol=symbol,
            timeframes=tf_reports,
            overall_trend=overall_trend,
            overall_regime=overall_regime,
            confidence=sum(x.scores.confidence for x in tf_reports.values()) / n,
            quality=sum(x.scores.quality for x in tf_reports.values()) / n,
            reliability=sum(x.scores.reliability for x in tf_reports.values()) / n,
        )
