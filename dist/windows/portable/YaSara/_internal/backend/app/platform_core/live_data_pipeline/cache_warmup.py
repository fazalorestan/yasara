class LiveDataCacheWarmupService:
    def warmup_plan(self):
        return {"ready": True, "symbols": ["BTCUSDT", "ETHUSDT", "BNBUSDT"], "mode": "simulated", "real_connection": False}

    def run(self):
        plan = self.warmup_plan()
        return {"ready": True, "warmed": True, "symbols": plan["symbols"], "real_connection": False}

live_data_cache_warmup_service = LiveDataCacheWarmupService()
