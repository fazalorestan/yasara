class LiveDataSnapshotCache:
    def __init__(self):
        self._cache = {}

    def put(self, key: str = "BTCUSDT", snapshot: dict | None = None):
        snapshot = snapshot or {"symbol": key, "price": 50000.0, "timestamp": 0}
        self._cache[key] = snapshot
        return {"ready": True, "cached": True, "key": key, "snapshot": snapshot}

    def get(self, key: str = "BTCUSDT"):
        snapshot = self._cache.get(key) or {"symbol": key, "price": 50000.0, "timestamp": 0}
        return {"ready": True, "hit": key in self._cache, "key": key, "snapshot": snapshot}

    def clear(self):
        self._cache.clear()
        return {"ready": True, "cleared": True}

live_data_snapshot_cache = LiveDataSnapshotCache()
