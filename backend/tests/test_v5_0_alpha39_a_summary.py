from app.v500_alpha39_live_data_core.models import LiveDataCoreSummaryV500Alpha39

def test_v500_alpha39_a_summary():
 s=LiveDataCoreSummaryV500Alpha39(); assert s.ready and s.test_pack_size==60