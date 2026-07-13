from app.platform_core.kernel.event_bus import PlatformEvent, event_bus

class LicenseAuditEventPublisher:
    def publish(self, action: str, payload: dict):
        event = PlatformEvent(
            name="LicenseAccessChecked",
            source="license_enforcement",
            payload={
                "action": action,
                "license_type": payload.get("license_type", "unknown"),
                "execution_allowed": False,
            },
        )
        event_bus.publish(event)
        return {"ready": True, "event": event.__dict__}

license_audit_event_publisher = LicenseAuditEventPublisher()
