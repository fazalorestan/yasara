from app.platform_core.alert_engine.severity import alert_severity_service

class AlertRuleEvaluator:
    def evaluate_scanner_candidate(self, candidate: dict):
        if float(candidate.get("score", 0)) >= 80:
            return {"ready": True, "triggered": True, "rule_id": "scanner_high_score", "severity": "warning", "message": f"High score candidate: {candidate.get('symbol')}"}
        return {"ready": True, "triggered": False, "rule_id": "scanner_high_score", "severity": "info", "message": "not_triggered"}

    def evaluate_risk_result(self, risk: dict):
        if risk.get("allowed") is False:
            return {"ready": True, "triggered": True, "rule_id": "risk_blocked", "severity": "critical", "message": risk.get("reason", "risk_blocked")}
        return {"ready": True, "triggered": False, "rule_id": "risk_blocked", "severity": "info", "message": "risk_ok"}

    def validate_event(self, event: dict):
        severity = alert_severity_service.validate(event.get("severity", "info"))
        return {"ready": severity["valid"], "severity": severity}

alert_rule_evaluator = AlertRuleEvaluator()
