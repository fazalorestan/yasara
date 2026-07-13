from app.platform_core.live_data_pipeline.cache_versioning import LiveDataCacheVersioningService

def test_v500_alpha39_d_tag(): assert LiveDataCacheVersioningService().tag_snapshot({'symbol':'BTCUSDT'})['snapshot']['cache_version']=='v1'
