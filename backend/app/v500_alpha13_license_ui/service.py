from app.platform_core.licensing.ui.service import license_ui_contract_service
from app.v500_alpha13_license_ui.models import LicenseUISummaryV500Alpha13

class LicenseUIFacadeV500Alpha13:
    def summary(self):
        return LicenseUISummaryV500Alpha13()

    def status_card(self, license_type: str = "demo"):
        return license_ui_contract_service.status_card(license_ui_contract_service.sample_payload(license_type))

    def countdown(self):
        return license_ui_contract_service.countdown(license_ui_contract_service.sample_payload("demo"))

    def feature_locks(self, license_type: str = "demo"):
        return license_ui_contract_service.feature_locks(license_ui_contract_service.sample_payload(license_type))

    def upgrade_prompt(self, feature: str = "ADVANCED_AI"):
        return license_ui_contract_service.upgrade_prompt(feature)

    def settings_page(self):
        return license_ui_contract_service.settings_page()

    def admin_panel(self):
        return license_ui_contract_service.admin_panel()

    def full_contract(self, license_type: str = "demo"):
        return license_ui_contract_service.full_ui_contract(license_ui_contract_service.sample_payload(license_type))
