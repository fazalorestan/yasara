from pydantic import BaseModel

class LiveDataCoreSummaryV500Alpha39(BaseModel):
    ready: bool = True
    phase: str = "v5_0_alpha_39_live_data_pipeline_package_a"
    scope: str = "data_source_core_ingestion_contract"
    data_source_registry: bool = True
    ingestion_contract: bool = True
    provider_adapter_contract: bool = True
    data_safety_policy: bool = True
    snapshot_normalizer: bool = True
    real_live_connection: bool = False
    real_execution_enabled: bool = False
    auto_trading_enabled: bool = False
    backward_compatible: bool = True
    test_pack_size: int = 60
