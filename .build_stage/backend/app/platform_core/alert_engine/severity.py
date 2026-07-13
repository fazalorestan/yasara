class AlertSeverityService:
    levels = ["info", "warning", "critical"]

    def validate(self, severity: str):
        return {"ready": True, "valid": severity in self.levels, "severity": severity}

    def priority(self, severity: str):
        return {"info": 1, "warning": 2, "critical": 3}.get(severity, 0)

alert_severity_service = AlertSeverityService()
