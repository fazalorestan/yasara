from app.v52_ai_first_dashboard.service import ai_first_dashboard_service
def test_contract():
    s = ai_first_dashboard_service.snapshot()
    assert s.real_data_only is True
    assert s.mock_data is False
