from app.v11_alerts.rule_engine import AlertRuleEngineV11

def test_ai_signal_alert():
    event = AlertRuleEngineV11().ai_signal("BTCUSDT", 0.8, "long")
    assert event.severity.value == "warning"
    assert event.payload["direction"] == "long"
