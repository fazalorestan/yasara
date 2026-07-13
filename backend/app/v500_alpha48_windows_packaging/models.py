from pydantic import BaseModel

class WindowsPackagingSummaryV500Alpha48(BaseModel):
    ready: bool = True
    phase: str = "v5_0_alpha_48_package_b"
    scope: str = "windows_packaging_contract"
    build_id: str = "2026.48.B.001"
    packaging_profile: bool = True
    portable_contract: bool = True
    installer_contract: bool = True
    app_metadata: bool = True
    output_layout: bool = True
    packaging_validation: bool = True
    exe_packaging_enabled: bool = False
    commercial_execution_engine_enabled: bool = False
    commercial_api_key_required: bool = False
    real_execution_enabled: bool = False
    real_broker_connection_enabled: bool = False
    backward_compatible: bool = True
    test_pack_size: int = 90
