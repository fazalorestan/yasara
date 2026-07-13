from app.v31_live_exchange.service import LiveExchangeServiceV31
from app.v49_market_structure.detectors import detect_swings
from app.v415_engine_registry_pro.registry import EngineRegistryProV415
from app.v417_elliott.detectors import (
    build_swing_points,
    classify_elliott_pattern,
    elliott_context_score,
    fibonacci_base,
    number_correction,
    number_impulse,
    parse_waves,
)
from app.v417_elliott.models import ElliottRequestV417, ElliottSummaryV417
from app.v417_elliott.rules import ElliottRuleRegistryV417

class ElliottEngineServiceV417:
    def __init__(self):
        self.live = LiveExchangeServiceV31()
        self.rules = ElliottRuleRegistryV417()
        self.registry = EngineRegistryProV415()

    def summary(self):
        return ElliottSummaryV417()

    def rule_registry(self):
        return self.rules.list()

    def analyze(self, request: ElliottRequestV417):
        candles = self.live.live_candles(request.symbol, request.exchange, request.timeframe, request.limit)["candles"]
        swings = detect_swings(candles, request.pivot_left, request.pivot_right)
        points = build_swing_points(swings)
        raw_waves = parse_waves(points)
        impulse = number_impulse(raw_waves)
        correction = number_correction(raw_waves)
        impulse_validation = self.rules.validate_impulse(impulse)
        correction_validation = self.rules.validate_correction(correction)
        fib = fibonacci_base(impulse if len(impulse) >= 5 else correction)
        pattern = classify_elliott_pattern(impulse_validation, correction_validation, impulse, correction)
        score = elliott_context_score(pattern, fib, impulse_validation, correction_validation)

        output = self.registry.normalize_output({
            "engine": "elliott",
            "version": "v4.17",
            "symbol": request.symbol.upper(),
            "exchange": request.exchange,
            "timeframe": request.timeframe,
            "bias": score["bias"],
            "confidence": score["score"],
            "reasons": score["reasons"],
            "payload": {
                "points": points,
                "raw_waves": raw_waves,
                "impulse_count": impulse,
                "correction_count": correction,
                "impulse_validation": impulse_validation,
                "correction_validation": correction_validation,
                "fibonacci_base": fib,
                "pattern": pattern,
                "context_score": score,
            },
        })

        return {
            "ready": True,
            "symbol": request.symbol.upper(),
            "exchange": request.exchange,
            "timeframe": request.timeframe,
            "elliott": output["payload"],
            "engine_output": output,
            "constitution_compliant": True,
            "real_order_execution_enabled": False,
            "live_trading_enabled": False,
        }

    def quick(self, symbol="BTCUSDT", exchange="binance", timeframe="1m"):
        return self.analyze(ElliottRequestV417(symbol=symbol, exchange=exchange, timeframe=timeframe))
