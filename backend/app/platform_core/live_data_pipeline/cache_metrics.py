class LiveDataCacheMetricsService:
    def metrics(self):
        return {
            "ready": True,
            "hits": 0,
            "misses": 0,
            "hit_rate": 0.0,
            "items": 0,
            "memory_mode": "in_memory_contract",
        }

live_data_cache_metrics_service = LiveDataCacheMetricsService()
