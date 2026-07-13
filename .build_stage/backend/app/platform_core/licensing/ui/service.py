from datetime import datetime, timedelta, timezone
from app.platform_core.licensing.features import feature_catalog
from app.platform_core.licensing.ui.admin_panel import license_admin_panel_contract
from app.platform_core.licensing.ui.countdown import demo_countdown_contract
from app.platform_core.licensing.ui.feature_lock import feature_lock_state_builder
from app.platform_core.licensing.ui.settings_contract import license_settings_page_contract
from app.platform_core.licensing.ui.status_card import license_status_card_contract
from app.platform_core.licensing.ui.upgrade_prompt import upgrade_prompt_contract

class LicenseUIContractService:
    def sample_payload(self, license_type: str = "demo"):
        return {
            "license_key": "LOCAL-UI",
            "license_type": license_type,
            "expires_at": (datetime.now(timezone.utc) + timedelta(days=30)).isoformat(),
        }

    def status_card(self, payload: dict):
        return license_status_card_contract.build(payload)

    def countdown(self, payload: dict):
        return demo_countdown_contract.build(payload)

    def feature_locks(self, payload: dict):
        return feature_lock_state_builder.build(payload, feature_catalog.features())

    def upgrade_prompt(self, feature: str):
        return upgrade_prompt_contract.prompt_for(feature)

    def settings_page(self):
        return license_settings_page_contract.contract()

    def admin_panel(self):
        return license_admin_panel_contract.contract()

    def full_ui_contract(self, payload: dict):
        return {
            "ready": True,
            "status_card": self.status_card(payload),
            "countdown": self.countdown(payload),
            "feature_locks": self.feature_locks(payload),
            "settings_page": self.settings_page(),
            "admin_panel": self.admin_panel(),
            "execution_allowed": False,
        }

license_ui_contract_service = LicenseUIContractService()
