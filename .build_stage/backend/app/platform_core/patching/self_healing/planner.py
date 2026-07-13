from app.platform_core.patching.self_healing.discovery import self_healing_patch_discovery
from app.platform_core.patching.self_healing.duplicates import patch_duplicate_detector
from app.platform_core.patching.self_healing.safety import self_healing_patch_safety
class SelfHealingPatchPlanner:
    def dry_run(self):
        scripts = self_healing_patch_discovery.discover()
        safety = [self_healing_patch_safety.validate(x["script"]) for x in scripts]
        duplicates = patch_duplicate_detector.detect(scripts)
        blocked = [x for x in safety if not x["allowed"]]
        return {"ready": len(blocked)==0 and duplicates["ready"],"total_scripts":len(scripts),"scripts":scripts,"safety":safety,"duplicates":duplicates,"blocked":blocked,"dry_run":True}
self_healing_patch_planner = SelfHealingPatchPlanner()
