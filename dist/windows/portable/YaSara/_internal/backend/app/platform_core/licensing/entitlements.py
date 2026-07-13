from app.platform_core.licensing.matrix import license_feature_matrix
from app.platform_core.licensing.validator import license_validator

class EntitlementEngine:
    def resolve(self, payload: dict):
        validation = license_validator.validate(payload)
        features = validation["features"] if validation["valid"] else []
        return {
            "ready": validation["valid"],
            "license_type": payload.get("license_type", "unknown"),
            "features": {feature: True for feature in features},
            "errors": validation["errors"],
        }

    def can_access(self, payload: dict, feature: str):
        resolved = self.resolve(payload)
        return {
            "ready": resolved["ready"],
            "feature": feature,
            "enabled": bool(resolved["features"].get(feature)),
            "reason": "enabled_by_license" if resolved["features"].get(feature) else "not_entitled",
        }

entitlement_engine = EntitlementEngine()
