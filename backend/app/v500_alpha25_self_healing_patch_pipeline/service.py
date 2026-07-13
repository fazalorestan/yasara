from app.platform_core.patching.self_healing.service import self_healing_patch_pipeline_service
from app.v500_alpha25_self_healing_patch_pipeline.models import SelfHealingPatchPipelineSummaryV500Alpha25
class SelfHealingPatchPipelineFacadeV500Alpha25:
    def summary(self): return SelfHealingPatchPipelineSummaryV500Alpha25()
    def discover(self): return self_healing_patch_pipeline_service.discover()
    def parse(self, script_name: str = "apply_v5_0_alpha_24_runtime_api_smoke_patch.py"): return self_healing_patch_pipeline_service.parse(script_name)
    def dry_run(self): return self_healing_patch_pipeline_service.dry_run()
    def manifest(self): return self_healing_patch_pipeline_service.manifest()
    def manifest_update_contract(self): return self_healing_patch_pipeline_service.manifest_update_contract("v5_0_alpha_25")
    def smoke(self): return self_healing_patch_pipeline_service.smoke()
    def verify_sample(self): return self_healing_patch_pipeline_service.verify_sample()
    def readiness(self): return self_healing_patch_pipeline_service.readiness()
    def contract(self): return {"ready": True, "purpose": "self_healing_patch_pipeline", "manual_patch_registration_required": False, "execution_allowed": False}
