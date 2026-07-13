from app.v500_alpha17_api_health.models import APIHealthSummaryV500Alpha17

def test_v500_alpha17_summary():
    s = APIHealthSummaryV500Alpha17()
    assert s.ready is True
    assert s.test_pack_size == 20
