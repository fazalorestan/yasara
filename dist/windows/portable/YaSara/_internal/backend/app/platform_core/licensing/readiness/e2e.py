from app.platform_core.licensing.designer import license_designer_contract
from app.platform_core.licensing.offline import offline_license_contract
from app.platform_core.licensing.entitlements import entitlement_engine
from app.platform_core.licensing.enforcement.service import license_enforcement_service
from app.platform_core.licensing.ui.service import license_ui_contract_service

class LicenseE2EFlow:
    def run_demo_flow(self):
        blob = license_designer_contract.create_demo()
        verify = offline_license_contract.verify(blob)
        payload = blob["payload"]
        entitlements = entitlement_engine.resolve(payload)
        feature_check = license_enforcement_service.check_feature(payload, "BASIC_ANALYSIS")
        ui = license_ui_contract_service.full_ui_contract(payload)
        return {
            "ready": verify["ready"] and entitlements["ready"] and feature_check["allowed"] and ui["ready"],
            "license_blob": blob,
            "verify": verify,
            "entitlements": entitlements,
            "feature_check": feature_check,
            "ui_ready": ui["ready"],
            "execution_allowed": False,
        }

license_e2e_flow = LicenseE2EFlow()
