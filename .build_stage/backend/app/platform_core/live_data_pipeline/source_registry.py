class LiveDataSourceRegistry:
    def __init__(self):
        self._sources = {
            "sim.exchange": {"source_id": "sim.exchange", "name": "Simulated Exchange Data", "mode": "simulated", "enabled": True},
            "sim.news": {"source_id": "sim.news", "name": "Simulated News Data", "mode": "simulated", "enabled": True},
        }

    def list_sources(self):
        return {"ready": True, "sources": list(self._sources.values()), "count": len(self._sources)}

    def get(self, source_id: str):
        source = self._sources.get(source_id)
        return {"ready": source is not None, "source": source}

    def register(self, source: dict):
        if not source.get("source_id"):
            return {"ready": False, "registered": False, "reason": "missing_source_id"}
        self._sources[source["source_id"]] = source
        return {"ready": True, "registered": True, "source_id": source["source_id"]}

live_data_source_registry = LiveDataSourceRegistry()
