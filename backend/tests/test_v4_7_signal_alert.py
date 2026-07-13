from app.v47_notification_alerts.models import SignalAlertRequestV47
from app.v47_notification_alerts.service import NotificationAlertEngineServiceV47

def test_v47_signal_alert():
    data = NotificationAlertEngineServiceV47().signal_alert_preview(SignalAlertRequestV47(min_confidence=0))
    assert data["ready"] is True
    assert "signal" in data
    assert data["real_order_execution_enabled"] is False
