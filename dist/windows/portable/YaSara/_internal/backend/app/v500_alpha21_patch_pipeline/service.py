from app.platform_core.patching.service import patch_pipeline_service
from app.v500_alpha21_patch_pipeline.models import PatchPipelineSummaryV500Alpha21
class PatchPipelineFacadeV500Alpha21:
    def summary(self): return PatchPipelineSummaryV500Alpha21()
    def discover(self): return patch_pipeline_service.discover()
    def classify(self, script_name: str = "apply_v5_0_alpha_20_launcher_api_search_patch.py"): return patch_pipeline_service.classify(script_name)
    def safety(self, script_name: str = "apply_v5_0_alpha_20_launcher_api_search_patch.py"): return patch_pipeline_service.safety(script_name)
    def plan(self): return patch_pipeline_service.plan()
    def readiness(self): return patch_pipeline_service.readiness()
    def contract(self): return {"ready": True, "goal": "yasara_patch_should_discover_v5_apply_scripts", "manual_v5_router_patch_required_after_this": False, "execution_allowed": False}
