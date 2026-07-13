from app.v500_alpha17_api_health.service import APIHealthFacadeV500Alpha17

def test_v500_alpha17_facade_contract():
    c = APIHealthFacadeV500Alpha17().contract()
    assert c['ready'] is True
    assert c['execution_allowed'] is False
