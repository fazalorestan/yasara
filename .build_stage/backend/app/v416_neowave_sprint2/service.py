from app.v415_neowave.service import NeoWaveEngineServiceV415
from app.v415_neowave.models import NeoWaveRequestV415
from app.v415_engine_registry_pro.registry import EngineRegistryProV415
from app.v416_neowave_sprint2.analyzers import (
    complexity_engine,
    pattern_confidence,
    price_rules,
    ratio_quality,
    time_rules,
    wave_ratios,
)
from app.v416_neowave_sprint2.models import NeoWaveSprint2RequestV416, NeoWaveSprint2SummaryV416

class NeoWaveSprint2ServiceV416:
    def __init__(self):
        self.v415 = NeoWaveEngineServiceV415()
        self.registry = EngineRegistryProV415()

    def summary(self):
        return NeoWaveSprint2SummaryV416()

    def analyze(self, request: NeoWaveSprint2RequestV416):
        base = self.v415.analyze(NeoWaveRequestV415(
            symbol=request.symbol,
            exchange=request.exchange,
            timeframe=request.timeframe,
            limit=request.limit,
        ))
        payload = base["neowave"]
        waves = payload.get("waves", [])
        validation = payload.get("validation", {})
        pattern = payload.get("pattern", {})

        ratios = wave_ratios(waves)
        complexity = complexity_engine(waves)
        time_rule = time_rules(waves)
        price_rule = price_rules(waves)
        ratio_q = ratio_quality(ratios)
        confidence = pattern_confidence(pattern, validation, complexity, time_rule, price_rule, ratio_q)

        output = self.registry.normalize_output({
            "engine": "neowave",
            "version": "v4.16",
            "symbol": request.symbol.upper(),
            "exchange": request.exchange,
            "timeframe": request.timeframe,
            "bias": confidence["bias"],
            "confidence": confidence["confidence"],
            "reasons": [
                f"complexity={complexity['level']}",
                f"time_valid={time_rule['valid']}",
                f"price_valid={price_rule['valid']}",
                f"ratio_quality={ratio_q['quality']}",
            ],
            "payload": {
                "base": payload,
                "wave_ratios": ratios,
                "complexity": complexity,
                "time_rules": time_rule,
                "price_rules": price_rule,
                "ratio_quality": ratio_q,
                "pattern_confidence": confidence,
            },
        })

        return {
            "ready": True,
            "symbol": request.symbol.upper(),
            "exchange": request.exchange,
            "timeframe": request.timeframe,
            "neowave_sprint2": output["payload"],
            "engine_output": output,
            "constitution_compliant": True,
            "real_order_execution_enabled": False,
            "live_trading_enabled": False,
        }

    def quick(self, symbol="BTCUSDT", exchange="binance", timeframe="1m"):
        return self.analyze(NeoWaveSprint2RequestV416(symbol=symbol, exchange=exchange, timeframe=timeframe))
