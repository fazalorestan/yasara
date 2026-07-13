from app.v47_notification_alerts.service import NotificationAlertEngineServiceV47

def test_v47_summary():
    s = NotificationAlertEngineServiceV47().summary()
    assert s.product_progress_percent == 98
    assert s.constitution_compliant is True
