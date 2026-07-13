from app.platform_core.licensing.features import feature_catalog
from app.platform_core.licensing.matrix import license_feature_matrix
from app.platform_core.licensing.types import license_types

class LicenseHealthCheck:
    def check(self):
        types = license_types.all()
        features = feature_catalog.features()
        missing = []
        for t in types:
            if t not in license_feature_matrix.matrix:
                missing.append(t)
        return {
            "ready": len(missing) == 0,
            "license_types_count": len(types),
            "features_count": len(features),
            "missing_matrix_entries": missing,
            "execution_allowed": False,
        }

license_health_check = LicenseHealthCheck()
