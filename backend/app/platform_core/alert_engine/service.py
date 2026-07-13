from app.platform_core.alert_engine.evaluator import alert_rule_evaluator
from app.platform_core.alert_engine.events import alert_event_builder
from app.platform_core.alert_engine.notification import alert_notification_contract
from app.platform_core.alert_engine.rules import alert_rule_registry
from app.platform_core.alert_engine.severity import alert_severity_service

class AlertEngineFoundationService:
    def rules(self): return {"ready": True, "rules": alert_rule_registry.default_rules()}
    def severity(self): return {"ready": True, "levels": alert_severity_service.levels}
    def channels(self): return alert_notification_contract.channels()

    def sample_scanner_alert(self):
        candidate = {"symbol": "BTCUSDT", "score": 82.0, "risk_pct": 1.0}
        result = alert_rule_evaluator.evaluate_scanner_candidate(candidate)
        if result["triggered"]:
            return alert_event_builder.build(result["rule_id"], candidate["symbol"], result["message"], result["severity"])
        return result

    def sample_risk_alert(self):
        risk = {"allowed": False, "reason": "max_daily_loss_exceeded"}
        result = alert_rule_evaluator.evaluate_risk_result(risk)
        if result["triggered"]:
            return alert_event_builder.build(result["rule_id"], "PORTFOLIO", result["message"], result["severity"])
        return result

    def notify_contract(self):
        event = self.sample_scanner_alert()
        return alert_notification_contract.send_contract(event)

    def summary_status(self):
        scanner = self.sample_scanner_alert()
        risk = self.sample_risk_alert()
        return {"ready": True, "triggered_count": int(scanner.get("ready", False)) + int(risk.get("ready", False)), "delivery_enabled": False, "execution_allowed": False}

alert_engine_foundation_service = AlertEngineFoundationService()
