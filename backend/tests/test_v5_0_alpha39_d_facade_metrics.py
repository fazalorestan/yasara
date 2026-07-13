from app.v500_alpha39_live_data_cache.service import LiveDataCacheFacadeV500Alpha39

def test_v500_alpha39_d_facade_metrics():
 r=LiveDataCacheFacadeV500Alpha39().metrics(); assert r is not None
