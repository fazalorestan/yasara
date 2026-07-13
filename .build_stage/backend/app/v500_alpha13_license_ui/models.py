from pydantic import BaseModel

class LicenseUISummaryV500Alpha13(BaseModel):
    ready: bool = True
    phase: str = "v5_0_alpha_13_license_ui_settings_integration"
    scope: str = "license_ui_contracts"
    settings_contract_supported: bool = True
    admin_panel_contract_supported: bool = True
    no_new_trading_features: bool = True
    live_execution_enabled: bool = False
    backward_compatible: bool = True
    test_pack_size: int = 20
