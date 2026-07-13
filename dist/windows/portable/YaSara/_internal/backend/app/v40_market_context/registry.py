class EngineRegistryV40:
    def __init__(self):
        self.engines = {
            "market_analysis": {"enabled": True, "weight": 1.2, "scope": "shared"},
            "smart_money": {"enabled": True, "weight": 1.1, "scope": "shared"},
            "advanced_ai_indicators": {"enabled": True, "weight": 1.0, "scope": "shared"},
            "strategy_builder": {"enabled": True, "weight": 0.8, "scope": "shared"},
            "autotrade_gate": {"enabled": True, "weight": 0.0, "scope": "personal_only", "commercial_included": False},
        }

    def list(self):
        return {"ready": True, "engines": self.engines, "live_trading_enabled": False}

    def enabled_engines(self):
        return {k: v for k, v in self.engines.items() if v.get("enabled")}
