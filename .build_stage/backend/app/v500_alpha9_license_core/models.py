from pydantic import BaseModel

class LicenseCoreSummaryV500Alpha9(BaseModel):
    ready: bool = True
    phase: str = "v5_0_alpha_9_license_entitlement_core"
    scope: str = "license_entitlement_foundation"
    demo_days_default: int = 30
    demo_days_short: int = 14
    no_new_trading_features: bool = True
    live_execution_enabled: bool = False
    backward_compatible: bool = True
    test_pack_size: int = 20
