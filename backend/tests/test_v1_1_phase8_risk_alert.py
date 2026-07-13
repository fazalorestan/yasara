from app.v11_alerts.rule_engine import AlertRuleEngineV11

def test_risk_alert_event():
    event = AlertRuleEngineV11().risk_block("blocked", "BTCUSDT")
    assert event.severity.value == "critical"
    assert event.source.value == "risk"
