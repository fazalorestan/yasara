from app.platform_core.live_data_pipeline.cache_ttl import LiveDataCacheTTLPolicy

def test_v500_alpha39_d_ttl(): assert LiveDataCacheTTLPolicy().policy()['enabled'] is True
