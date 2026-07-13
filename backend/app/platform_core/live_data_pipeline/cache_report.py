from app.platform_core.live_data_pipeline.cache_metrics import live_data_cache_metrics_service
from app.platform_core.live_data_pipeline.cache_ttl import live_data_cache_ttl_policy
from app.platform_core.live_data_pipeline.cache_versioning import live_data_cache_versioning_service
from app.platform_core.live_data_pipeline.cache_warmup import live_data_cache_warmup_service
from app.platform_core.live_data_pipeline.history_buffer import live_data_history_buffer
from app.platform_core.live_data_pipeline.snapshot_cache import live_data_snapshot_cache

class LiveDataCacheReportService:
    def report(self):
        put = live_data_snapshot_cache.put()
        get = live_data_snapshot_cache.get()
        history = live_data_history_buffer.append()
        return {
            "ready": True,
            "put": put,
            "get": get,
            "history": history,
            "ttl": live_data_cache_ttl_policy.policy(),
            "versioning": live_data_cache_versioning_service.version(),
            "warmup": live_data_cache_warmup_service.run(),
            "metrics": live_data_cache_metrics_service.metrics(),
            "real_connection": False,
            "execution_allowed": False,
        }

live_data_cache_report_service = LiveDataCacheReportService()
