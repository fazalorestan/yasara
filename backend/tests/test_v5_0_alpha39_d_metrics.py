from app.platform_core.live_data_pipeline.cache_metrics import LiveDataCacheMetricsService

def test_v500_alpha39_d_metrics(): assert LiveDataCacheMetricsService().metrics()['ready'] is True
