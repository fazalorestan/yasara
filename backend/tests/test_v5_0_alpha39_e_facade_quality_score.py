from app.v500_alpha39_live_data_enterprise.service import LiveDataEnterpriseFacadeV500Alpha39

def test_v500_alpha39_e_facade_quality_score():
 r=LiveDataEnterpriseFacadeV500Alpha39().quality_score(); assert r is not None
