from app.platform_core.indicators.alerts.adapter import indicator_signal_alert_adapter
from app.platform_core.indicators.alerts.deduplication import indicator_alert_deduplicator
from app.platform_core.indicators.alerts.notification_bridge import indicator_notification_bridge

class IndicatorAlertNotificationService:
    def build_alert(self, item: dict):
        alert = indicator_signal_alert_adapter.from_scanner_item(item)
        emit = indicator_alert_deduplicator.should_emit(alert["symbol"], alert["direction"], alert["confidence"])
        return {
            "ready": True,
            "alert": alert,
            "emit": emit and alert["severity"] != "silent",
            "execution_allowed": False,
            "mode": "analysis_only",
        }

    def publish_alert(self, item: dict):
        built = self.build_alert(item)
        if built["emit"]:
            built["notification"] = indicator_notification_bridge.publish(built["alert"])
        else:
            built["notification"] = None
        return built

indicator_alert_notification_service = IndicatorAlertNotificationService()
