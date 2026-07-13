class IndicatorAlertSeverity:
    def resolve(self, direction: str, confidence: int):
        if direction in ["LONG", "SHORT"] and confidence >= 85:
            return "critical"
        if direction in ["LONG", "SHORT"] and confidence >= 65:
            return "warning"
        if confidence >= 45:
            return "info"
        return "silent"

indicator_alert_severity = IndicatorAlertSeverity()
