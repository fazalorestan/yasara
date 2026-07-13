from app.platform_core.licensing.matrix import license_feature_matrix

class LicensePlanBuilder:
    def build(self, license_type: str, days: int | str = 30):
        return {
            "ready": True,
            "license_type": license_type,
            "duration": days,
            "features": license_feature_matrix.features_for(license_type),
            "device_limit": {"demo": 1, "personal": 1, "pro": 2, "elite": 3, "enterprise": 10, "lifetime": 3, "internal": 99}.get(license_type, 0),
            "execution_allowed": False,
        }

license_plan_builder = LicensePlanBuilder()
