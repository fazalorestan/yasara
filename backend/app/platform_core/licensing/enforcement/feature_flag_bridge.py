from app.platform_core.licensing.entitlements import entitlement_engine

class LicenseFeatureFlagBridge:
    def build_flags(self, payload: dict):
        resolved = entitlement_engine.resolve(payload)
        return {
            "ready": resolved["ready"],
            "license_type": resolved["license_type"],
            "flags": {f"feature.{k.lower()}": v for k, v in resolved["features"].items()},
            "errors": resolved["errors"],
        }

license_feature_flag_bridge = LicenseFeatureFlagBridge()
