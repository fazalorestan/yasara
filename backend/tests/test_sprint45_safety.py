from app.v52_ai_first_dashboard.service import ai_first_dashboard_service
def test_safety():
    s = ai_first_dashboard_service.snapshot()
    assert s.signal_only_default is True
    assert s.auto_trading_enabled is False
