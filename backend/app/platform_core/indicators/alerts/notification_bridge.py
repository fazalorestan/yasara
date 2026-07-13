from app.platform_core.kernel.event_bus import PlatformEvent, event_bus

class IndicatorNotificationBridge:
    def publish(self, alert: dict):
        event = PlatformEvent(
            name="IndicatorNotificationRequested",
            source="yasara_indicator",
            payload={
                "alert": alert,
                "execution_allowed": False,
                "mode": "analysis_only",
            },
        )
        event_bus.publish(event)
        return {"ready": True, "event": event.__dict__}

indicator_notification_bridge = IndicatorNotificationBridge()
