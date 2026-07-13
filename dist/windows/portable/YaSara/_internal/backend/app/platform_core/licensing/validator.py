from app.platform_core.licensing.matrix import license_feature_matrix
from app.platform_core.licensing.types import license_types

class LicenseValidator:
    def validate(self, payload: dict):
        errors = []
        license_type = payload.get("license_type", "unknown")
        if license_type not in license_types.all():
            errors.append("invalid_license_type")
        features = payload.get("features") or license_feature_matrix.features_for(license_type)
        if "AUTO_TRADING" in features and license_type not in ["internal"]:
            errors.append("auto_trading_requires_internal_license_at_this_stage")
        return {
            "valid": len(errors) == 0,
            "license_type": license_type,
            "features": features,
            "errors": errors,
            "warnings": [],
        }

license_validator = LicenseValidator()
