from app.platform_core.live_data_pipeline.cache_warmup import LiveDataCacheWarmupService

def test_v500_alpha39_d_warmup(): assert LiveDataCacheWarmupService().run()['warmed'] is True
