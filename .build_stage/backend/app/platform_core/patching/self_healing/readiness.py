from app.platform_core.patching.self_healing.planner import self_healing_patch_planner
from app.platform_core.patching.self_healing.smoke_contract import post_patch_smoke_contract
from app.platform_core.patching.self_healing.manifest import patch_manifest_manager
class SelfHealingPatchReadinessGate:
    def run(self):
        plan = self_healing_patch_planner.dry_run()
        smoke = post_patch_smoke_contract.checks()
        manifest = patch_manifest_manager.load()
        ready = plan["ready"] and smoke["ready"] and manifest.get("ready", True)
        return {"ready": ready, "score": 100.0 if ready else 0.0, "plan": plan, "smoke": smoke, "manifest": manifest}
self_healing_patch_readiness_gate = SelfHealingPatchReadinessGate()
