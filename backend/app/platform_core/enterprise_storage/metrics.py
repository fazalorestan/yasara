from app.platform_core.enterprise_storage.local import local_storage_engine

class StorageMetricsReporter:
    def report(self):
        records = local_storage_engine.list()
        buckets = {}
        for r in records:
            buckets[r["bucket"]] = buckets.get(r["bucket"], 0) + 1
        return {
            "ready": True,
            "record_count": len(records),
            "buckets": buckets,
            "mode": "local_report_only",
        }

storage_metrics_reporter = StorageMetricsReporter()
