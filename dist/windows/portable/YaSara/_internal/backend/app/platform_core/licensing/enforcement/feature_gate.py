from app.platform_core.licensing.entitlements import entitlement_engine

class LicenseFeatureGate:
    def check(self, payload: dict, feature: str):
        access = entitlement_engine.can_access(payload, feature)
        return {
            "ready": access["ready"],
            "feature": feature,
            "allowed": access["enabled"],
            "reason": access["reason"],
            "execution_allowed": False,
            "mode": "feature_gate",
        }

license_feature_gate = LicenseFeatureGate()
