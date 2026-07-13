from app.platform_core.live_data_pipeline.cache_ttl import LiveDataCacheTTLPolicy

def test_v500_alpha39_d_stale_false(): assert LiveDataCacheTTLPolicy().is_stale(0)['stale'] is False
