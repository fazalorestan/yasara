from app.platform_core.enterprise_cache.memory import enterprise_memory_cache

class CacheMetricsReporter:
    def report(self):
        snapshot = enterprise_memory_cache.snapshot()
        total_hits = sum(v.get("hits", 0) for v in snapshot.values())
        return {
            "ready": True,
            "item_count": len(snapshot),
            "total_hits": total_hits,
            "mode": "memory_report_only",
        }

cache_metrics_reporter = CacheMetricsReporter()
