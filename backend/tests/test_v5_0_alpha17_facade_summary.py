from app.v500_alpha17_api_health.service import APIHealthFacadeV500Alpha17

def test_v500_alpha17_facade_summary():
    assert APIHealthFacadeV500Alpha17().summary().ready is True
