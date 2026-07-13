from pathlib import Path
from app.platform_core.patching.self_healing.versioning import patch_version_parser
class SelfHealingPatchDiscovery:
    def __init__(self, scripts_dir: str = "scripts"):
        self.scripts_dir = Path(scripts_dir)
    def discover(self):
        if not self.scripts_dir.exists():
            return []
        items = [{"script":p.name,"path":str(p),"version":patch_version_parser.parse(p.name)} for p in self.scripts_dir.glob("apply_v*.py")]
        return sorted(items, key=lambda x: x["version"]["sort_key"])
self_healing_patch_discovery = SelfHealingPatchDiscovery()
