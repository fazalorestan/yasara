from pydantic import BaseModel

class LicenseManagerSummaryV500Alpha12(BaseModel):
    ready: bool = True
    phase: str = "v5_0_alpha_12_license_manager_admin_contract"
    scope: str = "license_manager_admin_foundation"
    admin_contract_supported: bool = True
    offline_export_supported: bool = True
    no_new_trading_features: bool = True
    live_execution_enabled: bool = False
    backward_compatible: bool = True
    test_pack_size: int = 20
