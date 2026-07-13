from app.v31_live_exchange.service import LiveExchangeServiceV31
from app.v49_market_structure.detectors import (
    context_score,
    detect_bos,
    detect_choch,
    detect_swings,
    premium_discount,
    range_state,
    trend_state,
)
from app.v49_market_structure.models import MarketStructureRequestV49, MarketStructureSummaryV49


class ProfessionalMarketStructureServiceV49:
    def __init__(self):
        self.live = LiveExchangeServiceV31()

    def summary(self):
        return MarketStructureSummaryV49()

    def analyze(self, request: MarketStructureRequestV49):
        payload = self.live.live_candles(
            symbol=request.symbol,
            exchange=request.exchange,
            timeframe=request.timeframe,
            limit=request.limit,
        )
        candles = payload["candles"]
        swings = detect_swings(candles, request.pivot_left, request.pivot_right)
        trend = trend_state(swings)
        bos = detect_bos(candles, swings)
        choch = detect_choch(candles, swings, trend)
        rng = range_state(candles)
        pd = premium_discount(candles)
        score = context_score(trend, bos, choch, rng, pd)

        return {
            "ready": True,
            "symbol": request.symbol.upper(),
            "exchange": request.exchange,
            "timeframe": request.timeframe,
            "structure": {
                "swings": {
                    "highs": swings["highs"][-10:],
                    "lows": swings["lows"][-10:],
                    "high_count": len(swings["highs"]),
                    "low_count": len(swings["lows"]),
                },
                "trend_state": trend,
                "break_of_structure": bos,
                "change_of_character": choch,
                "range_state": rng,
                "premium_discount": pd,
                "context_score": score,
            },
            "engine_output": {
                "engine": "market_structure_v4_9",
                "bias": score["bias"],
                "confidence": score["score"],
                "reasons": score["reasons"],
            },
            "constitution_compliant": True,
            "real_order_execution_enabled": False,
            "live_trading_enabled": False,
        }

    def quick(self, symbol="BTCUSDT", exchange="binance", timeframe="1m"):
        return self.analyze(MarketStructureRequestV49(symbol=symbol, exchange=exchange, timeframe=timeframe))
