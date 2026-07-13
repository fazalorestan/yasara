from app.productivity_v1.notification_rules import NotificationRuleEngineV1, NotificationRuleV1, NotificationChannel

def test_notification_rule_route():
    rules = [NotificationRuleV1(rule_id="r1", event_type="risk", channel=NotificationChannel.IN_APP)]
    result = NotificationRuleEngineV1().route(rules, "risk")
    assert result[0].rule_id == "r1"
