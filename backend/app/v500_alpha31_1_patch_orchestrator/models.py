from pydantic import BaseModel

class PatchOrchestratorSummaryV500Alpha311(BaseModel):
    ready: bool = True
    phase: str = "v5_0_alpha_31_1_patch_orchestrator_hotfix"
    scope: str = "patch_pipeline_hotfix"
    auto_discovery_enabled: bool = True
    manual_router_patch_required_after_this: bool = False
    destructive_patch_allowed: bool = False
    backward_compatible: bool = True
    test_pack_size: int = 15
