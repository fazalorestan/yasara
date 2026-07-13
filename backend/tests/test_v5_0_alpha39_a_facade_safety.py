from app.v500_alpha39_live_data_core.service import LiveDataCoreFacadeV500Alpha39

def test_v500_alpha39_a_facade_safety():
 r=LiveDataCoreFacadeV500Alpha39().safety(); assert r is not None
