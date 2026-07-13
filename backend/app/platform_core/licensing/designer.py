from app.platform_core.licensing.matrix import license_feature_matrix
from app.platform_core.licensing.offline import offline_license_contract

class LicenseDesignerContract:
    def create_demo(self, owner: str = "trial-user", days: int = 30):
        payload = {
            "license_key": "DEMO-YASARA-TRIAL",
            "license_type": "demo",
            "owner": owner,
            "features": license_feature_matrix.features_for("demo"),
            "duration_days": days,
            "device_limit": 1,
            "workspace_limit": 1,
            "alert_limit": 10,
        }
        return offline_license_contract.pack(payload)

    def design_contract(self):
        return {
            "ready": True,
            "license_types": ["demo", "personal", "pro", "elite", "enterprise", "lifetime", "internal"],
            "duration_options": [14, 30, 365, "lifetime"],
            "feature_selection": True,
            "device_limit": True,
            "workspace_limit": True,
            "alert_limit": True,
            "signed_payload_required": True,
        }

license_designer_contract = LicenseDesignerContract()
