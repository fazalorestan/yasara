from app.v49_market_structure.detectors import detect_swings
from app.v31_live_exchange.service import LiveExchangeServiceV31
from app.v415_engine_registry_pro.registry import EngineRegistryProV415
from app.v415_neowave.detectors import build_wave_points, build_waves, classify_pattern_skeleton, neowave_context_score
from app.v415_neowave.models import NeoWaveRequestV415, NeoWaveSummaryV415
from app.v415_neowave.rules import NeoWaveRuleRegistryV415

class NeoWaveEngineServiceV415:
    def __init__(self):
        self.live = LiveExchangeServiceV31()
        self.rules = NeoWaveRuleRegistryV415()
        self.registry = EngineRegistryProV415()

    def summary(self):
        return NeoWaveSummaryV415()

    def rule_registry(self):
        return self.rules.list()

    def analyze(self, request: NeoWaveRequestV415):
        candles = self.live.live_candles(request.symbol, request.exchange, request.timeframe, request.limit)["candles"]
        swings = detect_swings(candles, request.pivot_left, request.pivot_right)
        points = build_wave_points(swings)
        waves = build_waves(points)
        validation = self.rules.validate(waves)
        pattern = classify_pattern_skeleton(waves)
        score = neowave_context_score(validation, pattern)

        output = self.registry.normalize_output({
            "engine": "neowave",
            "version": "v4.15",
            "symbol": request.symbol.upper(),
            "exchange": request.exchange,
            "timeframe": request.timeframe,
            "bias": score["bias"],
            "confidence": score["score"],
            "reasons": score["reasons"],
            "payload": {
                "points": points,
                "waves": waves,
                "validation": validation,
                "pattern": pattern,
                "context_score": score,
            },
        })

        return {
            "ready": True,
            "symbol": request.symbol.upper(),
            "exchange": request.exchange,
            "timeframe": request.timeframe,
            "neowave": output["payload"],
            "engine_output": output,
            "constitution_compliant": True,
            "real_order_execution_enabled": False,
            "live_trading_enabled": False,
        }

    def quick(self, symbol="BTCUSDT", exchange="binance", timeframe="1m"):
        return self.analyze(NeoWaveRequestV415(symbol=symbol, exchange=exchange, timeframe=timeframe))
