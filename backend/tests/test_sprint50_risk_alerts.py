from app.productivity_v1.risk_alerts import RiskAlertEngineV1, RiskAlertInputV1

def test_risk_alert_critical():
    result = RiskAlertEngineV1().evaluate(RiskAlertInputV1(risk_score=90, exposure_percent=80))
    assert result.level == "critical"
    assert "risk_score_high" in result.warnings
