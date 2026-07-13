from app.platform_core.patching.classifier import patch_script_classifier
from app.platform_core.patching.discovery import patch_script_discovery
from app.platform_core.patching.planner import patch_pipeline_planner
from app.platform_core.patching.readiness import patch_pipeline_readiness_gate
from app.platform_core.patching.safety import patch_safety_filter
class PatchPipelineService:
    def discover(self): return {"ready": True, "scripts": patch_script_discovery.discover()}
    def classify(self, script_name: str): return patch_script_classifier.classify(script_name)
    def safety(self, script_name: str): return patch_safety_filter.allow(script_name)
    def plan(self): return patch_pipeline_planner.build_plan()
    def readiness(self): return patch_pipeline_readiness_gate.run()
patch_pipeline_service = PatchPipelineService()
