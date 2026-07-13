from app.platform_core.live_data_pipeline.cache_metrics import live_data_cache_metrics_service
from app.platform_core.live_data_pipeline.cache_readiness import live_data_cache_readiness_gate
from app.platform_core.live_data_pipeline.cache_report import live_data_cache_report_service
from app.platform_core.live_data_pipeline.cache_ttl import live_data_cache_ttl_policy
from app.platform_core.live_data_pipeline.cache_versioning import live_data_cache_versioning_service
from app.platform_core.live_data_pipeline.cache_warmup import live_data_cache_warmup_service
from app.platform_core.live_data_pipeline.history_buffer import live_data_history_buffer
from app.platform_core.live_data_pipeline.snapshot_cache import live_data_snapshot_cache
from app.v500_alpha39_live_data_cache.models import LiveDataCacheSummaryV500Alpha39

class LiveDataCacheFacadeV500Alpha39:
    def summary(self): return LiveDataCacheSummaryV500Alpha39()
    def put(self): return live_data_snapshot_cache.put()
    def get(self): return live_data_snapshot_cache.get()
    def history(self): return live_data_history_buffer.append()
    def latest(self): return live_data_history_buffer.latest()
    def ttl_policy(self): return live_data_cache_ttl_policy.policy()
    def stale_check(self): return live_data_cache_ttl_policy.is_stale(0)
    def version(self): return live_data_cache_versioning_service.version()
    def warmup(self): return live_data_cache_warmup_service.run()
    def metrics(self): return live_data_cache_metrics_service.metrics()
    def report(self): return live_data_cache_report_service.report()
    def readiness(self): return live_data_cache_readiness_gate.run()
    def contract(self): return {"ready": True, "live_data_pipeline": "package_d_snapshot_cache_history", "execution_allowed": False}

live_data_cache_facade_v500_alpha39 = LiveDataCacheFacadeV500Alpha39()
