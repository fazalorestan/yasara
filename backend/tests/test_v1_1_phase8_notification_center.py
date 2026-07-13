from app.v11_alerts.rule_engine import AlertRuleEngineV11
from app.v11_alerts.notification_center import NotificationCenterV11

def test_notification_center_delivery():
    event = AlertRuleEngineV11().risk_block("blocked", "BTCUSDT")
    deliveries = NotificationCenterV11().deliver(event)
    assert len(deliveries) == 2
    assert all(d.delivered for d in deliveries)
