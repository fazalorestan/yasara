from app.v500_alpha39_live_data_enterprise.models import LiveDataEnterpriseSummaryV500Alpha39

def test_v500_alpha39_e_summary():
 s=LiveDataEnterpriseSummaryV500Alpha39(); assert s.ready and s.test_pack_size==65
