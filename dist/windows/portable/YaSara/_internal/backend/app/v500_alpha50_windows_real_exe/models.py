from pydantic import BaseModel

class WindowsRealExeBuildPipelineSummaryV500Alpha50(BaseModel):
    ready: bool = True
    phase: str = "v5_0_alpha_50_package_a"
    scope: str = "first_real_windows_exe_build_pipeline"
    build_id: str = "2026.50.A.001"
    pyinstaller_contract: bool = True
    spec_contract: bool = True
    portable_builder: bool = True
    build_script_contract: bool = True
    artifact_hash_contract: bool = True
    smoke_test_contract: bool = True
    final_exe_generated: bool = False
    real_execution_enabled: bool = False
    real_broker_connection_enabled: bool = False
    commercial_execution_engine_enabled: bool = False
    commercial_api_key_required: bool = False
    backward_compatible: bool = True
    test_pack_size: int = 90
