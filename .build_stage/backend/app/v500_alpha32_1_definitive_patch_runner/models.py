from pydantic import BaseModel
class DefinitivePatchRunnerSummaryV500Alpha321(BaseModel):
    ready: bool = True
    phase: str = "v5_0_alpha_32_1_definitive_patch_runner_hotfix"
    scope: str = "patch_runner_hotfix"
    direct_patch_function_rewrite: bool = True
    auto_discovery_enabled: bool = True
    manual_router_patch_required_after_this: bool = False
    destructive_patch_allowed: bool = False
    backward_compatible: bool = True
    test_pack_size: int = 20
