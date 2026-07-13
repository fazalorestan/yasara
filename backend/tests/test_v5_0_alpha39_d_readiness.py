from app.platform_core.live_data_pipeline.cache_readiness import LiveDataCacheReadinessGate

def test_v500_alpha39_d_readiness(): assert LiveDataCacheReadinessGate().run()['ready'] is True
