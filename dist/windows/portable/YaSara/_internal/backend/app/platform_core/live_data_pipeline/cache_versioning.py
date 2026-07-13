class LiveDataCacheVersioningService:
    def version(self):
        return {"ready": True, "version": "v1", "schema": "snapshot-cache-v1"}

    def tag_snapshot(self, snapshot: dict):
        tagged = dict(snapshot)
        tagged["cache_version"] = self.version()["version"]
        return {"ready": True, "snapshot": tagged}

live_data_cache_versioning_service = LiveDataCacheVersioningService()
