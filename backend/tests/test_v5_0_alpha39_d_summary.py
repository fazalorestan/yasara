from app.v500_alpha39_live_data_cache.models import LiveDataCacheSummaryV500Alpha39

def test_v500_alpha39_d_summary():
 s=LiveDataCacheSummaryV500Alpha39(); assert s.ready and s.test_pack_size==60
