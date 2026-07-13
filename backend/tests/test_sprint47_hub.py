from app.v52_dashboard_provider_hub.service import dashboard_provider_hub
def test_hub():
    s=dashboard_provider_hub.snapshot()
    assert s.real_data_only is True
    assert s.mock_data is False
