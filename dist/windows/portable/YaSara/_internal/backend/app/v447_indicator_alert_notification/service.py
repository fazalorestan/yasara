from app.platform_core.indicators.alerts.service import indicator_alert_notification_service
from app.v447_indicator_alert_notification.models import IndicatorAlertNotificationSummaryV447

class IndicatorAlertNotificationFacadeV447:
    def summary(self):
        return IndicatorAlertNotificationSummaryV447()

    def sample_alert(self):
        item = {"symbol": "BTCUSDT", "direction": "LONG", "score": 88}
        return indicator_alert_notification_service.build_alert(item)

    def sample_publish(self):
        item = {"symbol": "ETHUSDT", "direction": "SHORT", "score": 72}
        return indicator_alert_notification_service.publish_alert(item)

    def contract(self):
        return {
            "ready": True,
            "input": ["symbol", "direction", "score"],
            "output": ["id", "indicator", "symbol", "direction", "confidence", "severity", "message"],
            "events": ["IndicatorNotificationRequested"],
            "execution_allowed": False,
            "mode": "analysis_only",
        }
