try:
    from app.v31_live_exchange.service import LiveExchangeServiceV31
except Exception:
    LiveExchangeServiceV31 = None

from app.v421_market_structure_pro.detectors import chart_annotations, confirmed_swings, detect_bos_choch, range_state, score_structure, structure_bias, trend_state
from app.v421_market_structure_pro.models import MarketStructureProRequestV421, MarketStructureProSummaryV421

class MarketStructureProServiceV421:
    def __init__(self):
        self.live = LiveExchangeServiceV31() if LiveExchangeServiceV31 else None

    def summary(self):
        return MarketStructureProSummaryV421()

    def _fallback_candles(self, limit=240):
        candles = []
        price = 50000.0
        for i in range(limit):
            wave = ((i % 30) - 15) * 18
            drift = i * 2
            open_price = price + wave + drift
            close = open_price + ((i % 7) - 3) * 12
            high = max(open_price, close) + 70 + (i % 5) * 6
            low = min(open_price, close) - 70 - (i % 4) * 6
            candles.append({"time": i, "open": round(open_price, 4), "high": round(high, 4), "low": round(low, 4), "close": round(close, 4), "volume": 1000 + i * 5})
        return candles

    def _candles(self, request):
        if self.live:
            try:
                return self.live.live_candles(request.symbol, request.exchange, request.timeframe, request.limit)["candles"]
            except Exception:
                pass
        return self._fallback_candles(request.limit)

    def analyze(self, request: MarketStructureProRequestV421):
        candles = self._candles(request)
        swings = confirmed_swings(candles, request.pivot_left, request.pivot_right)
        events = detect_bos_choch(candles, swings)
        trend = trend_state(events)
        range_info = range_state(candles, swings, request.range_tolerance_percent)
        bias = structure_bias(trend, range_info)
        structure_score = score_structure(bias, events, range_info)
        annotations = chart_annotations(swings, events, range_info)
        return {
            "ready": True,
            "symbol": request.symbol.upper(),
            "exchange": request.exchange,
            "timeframe": request.timeframe,
            "market_structure_pro": {
                "swings": swings,
                "events": events,
                "trend_state": trend,
                "range_state": range_info,
                "structure_bias": bias,
                "structure_score": structure_score,
                "chart_annotations": annotations,
            },
            "engine_output": {
                "engine": "market_structure_pro",
                "version": "v4.21",
                "symbol": request.symbol.upper(),
                "exchange": request.exchange,
                "timeframe": request.timeframe,
                "bias": structure_score["bias"],
                "confidence": structure_score["score"],
                "reasons": structure_score["reasons"],
                "payload": {"event_count": len(events), "swing_count": swings["count"], "annotation_count": len(annotations), "market_mode": bias["market_mode"]},
                "real_order_execution_enabled": False,
                "live_trading_enabled": False,
            },
            "constitution_compliant": True,
            "real_order_execution_enabled": False,
            "live_trading_enabled": False,
        }

    def quick(self, symbol="BTCUSDT", exchange="binance", timeframe="15m"):
        return self.analyze(MarketStructureProRequestV421(symbol=symbol, exchange=exchange, timeframe=timeframe))
