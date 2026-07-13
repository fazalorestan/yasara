from pydantic import BaseModel
class PatchPipelineSummaryV500Alpha21(BaseModel):
    ready: bool = True
    phase: str = "v5_0_alpha_21_patch_pipeline_autodiscovery"
    scope: str = "patch_pipeline_autodiscovery"
    v5_auto_discovery_enabled: bool = True
    destructive_patch_allowed: bool = False
    auto_trading_enabled: bool = False
    real_exchange_connection: bool = False
    backward_compatible: bool = True
    test_pack_size: int = 20
