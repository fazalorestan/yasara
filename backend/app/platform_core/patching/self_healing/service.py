from app.platform_core.patching.self_healing.discovery import self_healing_patch_discovery
from app.platform_core.patching.self_healing.manifest import patch_manifest_manager
from app.platform_core.patching.self_healing.planner import self_healing_patch_planner
from app.platform_core.patching.self_healing.readiness import self_healing_patch_readiness_gate
from app.platform_core.patching.self_healing.smoke_contract import post_patch_smoke_contract
from app.platform_core.patching.self_healing.versioning import patch_version_parser
from app.platform_core.patching.self_healing.verification import patch_verification_contract
class SelfHealingPatchPipelineService:
    def discover(self): return {"ready": True, "scripts": self_healing_patch_discovery.discover()}
    def parse(self, script_name: str): return patch_version_parser.parse(script_name)
    def dry_run(self): return self_healing_patch_planner.dry_run()
    def manifest(self): return patch_manifest_manager.load()
    def manifest_update_contract(self, patch_name: str): return patch_manifest_manager.update_contract(patch_name)
    def smoke(self): return post_patch_smoke_contract.checks()
    def verify_sample(self): return patch_verification_contract.verify_router_patch("api_router.include_router(v500_alpha25_self_healing_patch_pipeline_v1.router)", "v500_alpha25_self_healing_patch_pipeline_v1")
    def readiness(self): return self_healing_patch_readiness_gate.run()
self_healing_patch_pipeline_service = SelfHealingPatchPipelineService()
