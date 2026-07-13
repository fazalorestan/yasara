from app.platform_core.licensing.enforcement.service import license_enforcement_service
from app.v500_alpha10_license_enforcement.models import LicenseEnforcementSummaryV500Alpha10

class LicenseEnforcementFacadeV500Alpha10:
    def summary(self):
        return LicenseEnforcementSummaryV500Alpha10()

    def demo_payload(self):
        return {"license_key": "DEMO-YASARA-TRIAL", "license_type": "demo"}

    def pro_payload(self):
        return {"license_key": "PRO-LOCAL", "license_type": "pro"}

    def check_feature(self, feature: str = "BASIC_ANALYSIS", license_type: str = "demo"):
        return license_enforcement_service.check_feature({"license_type": license_type}, feature)

    def flags(self, license_type: str = "demo"):
        return license_enforcement_service.build_flags({"license_type": license_type})

    def check_plugin(self, plugin: str = "yasara_indicator", license_type: str = "demo"):
        return license_enforcement_service.check_plugin({"license_type": license_type}, plugin)

    def demo_usage(self, alerts: int = 0, indicators: int = 1, workspaces: int = 1):
        return license_enforcement_service.check_demo_usage({"alerts": alerts, "indicators": indicators, "workspaces": workspaces})

    def usage(self):
        return license_enforcement_service.usage()

    def contract(self):
        return {
            "ready": True,
            "flow": ["license_payload", "entitlement_engine", "feature_gate", "plugin_guard", "usage_counter", "audit_event"],
            "demo_limits_enforced": True,
            "execution_allowed": False,
        }
