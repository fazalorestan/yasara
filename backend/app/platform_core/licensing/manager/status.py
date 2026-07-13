from app.platform_core.licensing.entitlements import entitlement_engine
from app.platform_core.licensing.activation.expiry import license_expiry_checker

class LicenseStatusReporter:
    def status(self, payload: dict):
        entitlement = entitlement_engine.resolve(payload)
        expiry = license_expiry_checker.status(payload)
        return {
            "ready": entitlement["ready"] and expiry["ready"],
            "license_type": payload.get("license_type", "unknown"),
            "features_count": len(entitlement.get("features", {})),
            "expired": expiry["expired"],
            "valid_time": expiry["valid_time"],
            "errors": entitlement.get("errors", []),
            "execution_allowed": False,
        }

license_status_reporter = LicenseStatusReporter()
