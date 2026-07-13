from app.v52_dashboard_provider_hub.service import dashboard_provider_hub
def test_guard():
    s=dashboard_provider_hub.snapshot()
    assert s.approved_dashboard_locked is True
    assert s.auto_trading_enabled is False
