from app.platform_core.alert_engine.service import alert_engine_foundation_service

class AlertEngineReadinessGate:
    def run(self):
        rules = alert_engine_foundation_service.rules()
        channels = alert_engine_foundation_service.channels()
        status = alert_engine_foundation_service.summary_status()
        ready = rules["ready"] and channels["ready"] and status["ready"]
        return {"ready": ready, "checks": {"rules_ready": rules["ready"], "channels_ready": channels["ready"], "status_ready": status["ready"], "delivery_enabled": False, "real_execution_allowed": False, "auto_trading_allowed": False}, "execution_allowed": False}

alert_engine_readiness_gate = AlertEngineReadinessGate()
