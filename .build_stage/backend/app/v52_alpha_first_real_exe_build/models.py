from pydantic import BaseModel
class FirstRealExeBuildSummaryV52Alpha(BaseModel):
    ready: bool = True
    phase: str = 'v5_2_alpha_package_b'
    build_id: str = '2026.52.B.001'
    environment_validation: bool = True
    dependency_lock: bool = True
    asset_collection: bool = True
    backend_packaging: bool = True
    frontend_packaging: bool = True
    exe_generation: bool = True
    artifact_generation: bool = True
    smoke_test: bool = True
    signal_only_default: bool = True
    auto_trading_enabled: bool = False
    real_execution_enabled: bool = False
    real_broker_connection_enabled: bool = False
    test_pack_size: int = 90
