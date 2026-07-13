from app.platform_core.clock import utc_now_iso

class AlertEventBuilder:
    def build(self, rule_id: str, symbol: str, message: str, severity: str):
        return {"ready": True, "rule_id": rule_id, "symbol": symbol, "message": message, "severity": severity, "triggered_at": utc_now_iso(), "acknowledged": False}

alert_event_builder = AlertEventBuilder()
