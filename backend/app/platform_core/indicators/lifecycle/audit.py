from app.platform_core.kernel.event_bus import PlatformEvent, event_bus

class IndicatorLifecycleAuditPublisher:
    def publish(self, indicator: str, action: str, state: str):
        event = PlatformEvent(
            name="IndicatorLifecycleChanged",
            source="indicator_lifecycle",
            payload={
                "indicator": indicator,
                "action": action,
                "state": state,
                "execution_allowed": False,
            },
        )
        event_bus.publish(event)
        return {"ready": True, "event": event.__dict__}

indicator_lifecycle_audit_publisher = IndicatorLifecycleAuditPublisher()
