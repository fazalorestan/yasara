from pathlib import Path
class PatchScriptDiscovery:
    def __init__(self, scripts_dir: str = "scripts"):
        self.scripts_dir = Path(scripts_dir)
    def discover(self):
        if not self.scripts_dir.exists():
            return []
        return sorted([p.name for p in self.scripts_dir.glob("apply_*.py") if p.is_file()])
patch_script_discovery = PatchScriptDiscovery()
