from app.platform_core.patching.classifier import patch_script_classifier
from app.platform_core.patching.discovery import patch_script_discovery
class PatchPipelinePlanner:
    def build_plan(self):
        scripts = patch_script_discovery.discover()
        items = [patch_script_classifier.classify(s) for s in scripts]
        safe = [i for i in items if i["safe"]]
        v5 = [i for i in safe if i["family"] == "v5"]
        return {"ready": True, "total_scripts": len(scripts), "safe_scripts": len(safe), "v5_scripts": len(v5), "items": items, "v5_auto_discovery_enabled": True}
patch_pipeline_planner = PatchPipelinePlanner()
