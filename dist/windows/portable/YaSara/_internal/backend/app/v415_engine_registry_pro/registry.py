class EngineRegistryProV415:
    def __init__(self):
        self.engines = {
            "market_context": {"enabled": True, "category": "context", "weight": 1.05},
            "market_structure": {"enabled": True, "category": "structure", "weight": 1.25},
            "smart_money": {"enabled": True, "category": "smc", "weight": 1.35},
            "ict": {"enabled": True, "category": "ict", "weight": 1.25},
            "indicator": {"enabled": True, "category": "indicator", "weight": 0.85},
            "risk": {"enabled": True, "category": "risk", "weight": 1.10},
            "ai_fusion": {"enabled": True, "category": "fusion", "weight": 1.4},
            "neowave": {"enabled": True, "category": "wave", "weight": 1.15},
        }

    def list(self):
        return {"ready": True, "engines": self.engines, "count": len(self.engines), "live_trading_enabled": False}

    def get_weight(self, engine):
        return self.engines.get(engine, {}).get("weight", 1.0)

    def normalize_output(self, output):
        return {
            "engine": output.get("engine", "unknown"),
            "version": output.get("version", "v4.15"),
            "symbol": output.get("symbol", "BTCUSDT"),
            "exchange": output.get("exchange", "binance"),
            "timeframe": output.get("timeframe", "1m"),
            "bias": output.get("bias", "neutral"),
            "confidence": max(0, min(100, float(output.get("confidence", 50)))),
            "reasons": output.get("reasons", []),
            "payload": output.get("payload", {}),
            "weight": self.get_weight(output.get("engine", "unknown")),
            "real_order_execution_enabled": False,
            "live_trading_enabled": False,
        }
