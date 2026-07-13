from uuid import uuid4
from app.platform_core.indicators.alerts.models import IndicatorAlertPayload
from app.platform_core.indicators.alerts.severity import indicator_alert_severity

class IndicatorSignalAlertAdapter:
    def from_scanner_item(self, item: dict):
        direction = item.get("direction", "WAIT")
        confidence = int(item.get("score", item.get("confidence", 0)))
        severity = indicator_alert_severity.resolve(direction, confidence)
        return IndicatorAlertPayload(
            id=str(uuid4()),
            symbol=item.get("symbol", "UNKNOWN"),
            direction=direction,
            confidence=confidence,
            severity=severity,
            message=f"YaSara {direction} {confidence}% on {item.get('symbol', 'UNKNOWN')}",
            metadata={"source": "indicator_scanner"},
        ).__dict__

indicator_signal_alert_adapter = IndicatorSignalAlertAdapter()
