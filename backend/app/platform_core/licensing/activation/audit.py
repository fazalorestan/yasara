from app.platform_core.kernel.event_bus import PlatformEvent, event_bus

class LicenseActivationAuditPublisher:
    def publish(self, action: str, license_type: str):
        event = PlatformEvent(
            name="LicenseActivationChanged",
            source="license_activation",
            payload={
                "action": action,
                "license_type": license_type,
                "execution_allowed": False,
            },
        )
        event_bus.publish(event)
        return {"ready": True, "event": event.__dict__}

license_activation_audit_publisher = LicenseActivationAuditPublisher()
