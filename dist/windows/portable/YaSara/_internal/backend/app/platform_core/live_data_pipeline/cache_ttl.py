class LiveDataCacheTTLPolicy:
    def policy(self):
        return {"ready": True, "ttl_ms": 30000, "stale_after_ms": 60000, "enabled": True}

    def is_stale(self, age_ms: int):
        ttl = self.policy()["ttl_ms"]
        return {"ready": True, "age_ms": age_ms, "stale": age_ms > ttl}

live_data_cache_ttl_policy = LiveDataCacheTTLPolicy()
