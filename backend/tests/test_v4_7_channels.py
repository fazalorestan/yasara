from app.v47_notification_alerts.service import NotificationAlertEngineServiceV47

def test_v47_channels():
    data = NotificationAlertEngineServiceV47().channel_status()
    assert data["ready"] is True
    assert "telegram" in data["channels"]
