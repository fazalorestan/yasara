from pydantic import BaseModel

class LicenseActivationSummaryV500Alpha11(BaseModel):
    ready: bool = True
    phase: str = "v5_0_alpha_11_license_activation_device_binding"
    scope: str = "license_activation_foundation"
    offline_activation_supported: bool = True
    device_binding_supported: bool = True
    no_new_trading_features: bool = True
    live_execution_enabled: bool = False
    backward_compatible: bool = True
    test_pack_size: int = 20
