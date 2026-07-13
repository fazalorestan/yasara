from app.v47_notification_alerts.service import NotificationAlertEngineServiceV47

def test_v47_risk_alert():
    data = NotificationAlertEngineServiceV47().risk_alert_preview()
    assert data["ready"] is True
    assert "risk" in data
