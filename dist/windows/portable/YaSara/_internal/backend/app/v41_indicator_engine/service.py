from app.v31_live_exchange.service import LiveExchangeServiceV31
from app.v41_indicator_engine.models import IndicatorEngineSummaryV41, IndicatorRequestV41, IndicatorResultV41
from app.v41_indicator_engine.registry import ModularIndicatorRegistryV41


class ModularIndicatorEngineServiceV41:
    def __init__(self):
        self.live = LiveExchangeServiceV31()
        self.registry = ModularIndicatorRegistryV41()

    def summary(self):
        return IndicatorEngineSummaryV41()

    def registry_status(self):
        return {
            "ready": True,
            "indicators": self.registry.names(),
            "count": len(self.registry.names()),
            "modular": True,
            "live_trading_enabled": False,
        }

    def analyze(self, request: IndicatorRequestV41):
        payload = self.live.live_candles(
            symbol=request.symbol,
            exchange=request.exchange,
            timeframe=request.timeframe,
            limit=request.limit,
        )
        candles = payload["candles"]
        results = []
        for name in request.indicators:
            if name not in self.registry.registry:
                continue
            value, bias, confidence = self.registry.compute(name, candles)
            results.append(IndicatorResultV41(name=name, value=value, bias=bias, confidence=confidence).model_dump())

        bullish = sum(1 for r in results if r["bias"] == "bullish")
        bearish = sum(1 for r in results if r["bias"] == "bearish")
        bias = "bullish" if bullish > bearish else "bearish" if bearish > bullish else "neutral"
        confidence = round(max(bullish, bearish, 1) / max(len(results), 1) * 100, 2)

        return {
            "ready": True,
            "symbol": request.symbol.upper(),
            "exchange": request.exchange,
            "timeframe": request.timeframe,
            "results": results,
            "aggregate": {
                "bias": bias,
                "confidence": confidence,
                "bullish_count": bullish,
                "bearish_count": bearish,
                "neutral_count": len(results) - bullish - bearish,
            },
            "constitution_compliant": True,
            "live_trading_enabled": False,
        }

    def quick(self, symbol: str = "BTCUSDT", exchange: str = "binance", timeframe: str = "1m"):
        return self.analyze(IndicatorRequestV41(symbol=symbol, exchange=exchange, timeframe=timeframe))
