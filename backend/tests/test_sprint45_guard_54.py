from app.v52_ai_first_dashboard.service import ai_first_dashboard_service
def test_guard():
    s = ai_first_dashboard_service.snapshot()
    assert s.mock_data is False
