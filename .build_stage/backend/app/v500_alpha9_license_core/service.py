from app.platform_core.licensing.designer import license_designer_contract
from app.platform_core.licensing.entitlements import entitlement_engine
from app.platform_core.licensing.features import feature_catalog
from app.platform_core.licensing.matrix import license_feature_matrix
from app.platform_core.licensing.offline import offline_license_contract
from app.platform_core.licensing.parser import license_key_parser
from app.platform_core.licensing.plugin_requirements import plugin_license_requirement_service
from app.platform_core.licensing.trial import trial_policy
from app.platform_core.licensing.validator import license_validator
from app.v500_alpha9_license_core.models import LicenseCoreSummaryV500Alpha9

class LicenseCoreFacadeV500Alpha9:
    def summary(self):
        return LicenseCoreSummaryV500Alpha9()

    def trial_policy(self):
        return trial_policy.policy()

    def feature_catalog(self):
        return {"ready": True, "features": feature_catalog.features()}

    def matrix(self):
        return {"ready": True, "matrix": license_feature_matrix.matrix}

    def parse_key(self, key: str = "DEMO-YASARA-TRIAL"):
        return license_key_parser.parse_visual_format(key)

    def create_demo(self):
        return license_designer_contract.create_demo()

    def verify_demo(self):
        blob = license_designer_contract.create_demo()
        return offline_license_contract.verify(blob)

    def entitlements(self, license_type: str = "demo"):
        payload = {"license_key": "LOCAL", "license_type": license_type}
        return entitlement_engine.resolve(payload)

    def can_access(self, feature: str = "BASIC_ANALYSIS", license_type: str = "demo"):
        payload = {"license_key": "LOCAL", "license_type": license_type}
        return entitlement_engine.can_access(payload, feature)

    def plugin_requirement(self, plugin: str = "yasara_indicator"):
        return plugin_license_requirement_service.requirement_for(plugin)

    def designer_contract(self):
        return license_designer_contract.design_contract()

    def contract(self):
        return {
            "ready": True,
            "flow": ["signature_validation", "license_parser", "entitlement_engine", "feature_flags", "permissions", "plugin_registry"],
            "demo_supported": True,
            "offline_license_supported": True,
            "online_license_future_ready": True,
            "execution_allowed": False,
        }
