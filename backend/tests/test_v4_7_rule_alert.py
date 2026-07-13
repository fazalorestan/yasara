from app.v47_notification_alerts.models import AlertEventV47, AlertRuleV47
from app.v47_notification_alerts.service import NotificationAlertEngineServiceV47

def test_v47_rule_alert():
    s = NotificationAlertEngineServiceV47()
    rule = s.add_rule(AlertRuleV47(id="test-rule-v47", name="Test Rule"))
    alert = s.create_alert(AlertEventV47(id="test-alert-v47", title="Test", message="Hello"))
    assert rule["ready"] is True
    assert alert["ready"] is True
    assert alert["real_order_execution_enabled"] is False
