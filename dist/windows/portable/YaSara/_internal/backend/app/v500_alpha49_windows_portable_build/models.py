from pydantic import BaseModel

class WindowsPortableBuildSummaryV500Alpha49(BaseModel):
    ready: bool = True
    phase: str = "v5_0_alpha_49_package_d"
    scope: str = "first_internal_windows_portable_build_contract"
    build_id: str = "2026.49.D.001"
    portable_build_layout: bool = True
    internal_build_manifest: bool = True
    build_script_contract: bool = True
    artifact_registration_contract: bool = True
    launch_smoke_contract: bool = True
    final_exe_generated: bool = False
    artifact_registered: bool = False
    real_execution_enabled: bool = False
    real_broker_connection_enabled: bool = False
    commercial_execution_engine_enabled: bool = False
    commercial_api_key_required: bool = False
    backward_compatible: bool = True
    test_pack_size: int = 90
