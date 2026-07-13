from pathlib import Path
import json
class PatchManifestManager:
    def __init__(self, manifest_path: str = "patch_manifest.json"):
        self.manifest_path = Path(manifest_path)
    def default(self):
        return {"ready": True, "last_patch": None, "installed": [], "failed": []}
    def load(self):
        if not self.manifest_path.exists():
            return self.default()
        try:
            return json.loads(self.manifest_path.read_text(encoding="utf-8"))
        except Exception:
            return self.default() | {"manifest_recovered": True}
    def update_contract(self, patch_name: str):
        m = self.load()
        installed = list(dict.fromkeys(m.get("installed", []) + [patch_name]))
        return {"ready": True, "last_patch": patch_name, "installed": installed, "failed": m.get("failed", [])}
patch_manifest_manager = PatchManifestManager()
