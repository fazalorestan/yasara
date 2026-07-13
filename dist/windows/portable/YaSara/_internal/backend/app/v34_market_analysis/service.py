from app.v31_live_exchange.service import LiveExchangeServiceV31
from app.v34_market_analysis.detectors import (
    analyze_volume,
    detect_momentum,
    detect_range,
    detect_regime,
    detect_trend,
    detect_volatility,
    session_analysis,
)
from app.v34_market_analysis.models import MarketAnalysisRequestV34, MarketAnalysisSummaryV34


class MarketAnalysisEngineServiceV34:
    def __init__(self):
        self.live = LiveExchangeServiceV31()

    def summary(self):
        return MarketAnalysisSummaryV34()

    def analyze_timeframe(self, symbol: str, exchange: str, timeframe: str, limit: int):
        payload = self.live.live_candles(symbol=symbol, exchange=exchange, timeframe=timeframe, limit=limit)
        candles = payload["candles"]
        closes = [c["close"] for c in candles]
        trend = detect_trend(closes)
        range_data = detect_range(candles)
        volatility = detect_volatility(candles)
        momentum = detect_momentum(closes)
        volume = analyze_volume(candles)
        regime = detect_regime(trend, range_data, volatility, momentum)
        session = session_analysis(payload["ts"])

        return {
            "timeframe": timeframe,
            "trend": trend,
            "range": range_data,
            "volatility": volatility,
            "momentum": momentum,
            "volume": volume,
            "regime": regime,
            "session": session,
            "last_close": closes[-1] if closes else 0,
            "source": "v34_market_analysis_engine",
        }

    def analyze(self, request: MarketAnalysisRequestV34):
        enabled = request.feature_flags
        timeframe_results = []
        for tf in request.timeframes:
            timeframe_results.append(self.analyze_timeframe(request.symbol, request.exchange, tf, request.limit))

        bullish = sum(1 for item in timeframe_results if item["trend"]["trend"] == "bullish")
        bearish = sum(1 for item in timeframe_results if item["trend"]["trend"] == "bearish")
        ranging = sum(1 for item in timeframe_results if item["regime"] == "range")

        dominant_bias = "bullish" if bullish > bearish else "bearish" if bearish > bullish else "neutral"
        dominant_regime = "range" if ranging >= len(timeframe_results) / 2 else "trend_or_mixed"

        alignment_score = round(max(bullish, bearish, ranging) / max(len(timeframe_results), 1) * 100, 2)

        return {
            "ready": True,
            "symbol": request.symbol.upper(),
            "exchange": request.exchange,
            "timeframes": request.timeframes,
            "feature_flags": enabled,
            "multi_timeframe": timeframe_results,
            "market_context": {
                "dominant_bias": dominant_bias,
                "dominant_regime": dominant_regime,
                "alignment_score": alignment_score,
                "analysis_quality": "good" if alignment_score >= 60 else "mixed",
            },
            "constitution_compliant": True,
            "live_trading_enabled": False,
        }

    def quick(self, symbol: str = "BTCUSDT", exchange: str = "binance"):
        return self.analyze(MarketAnalysisRequestV34(symbol=symbol, exchange=exchange))
