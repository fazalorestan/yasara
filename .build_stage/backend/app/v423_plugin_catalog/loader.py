import json
from pathlib import Path
from app.platform_core.paths import plugin_manifest_root
from app.v423_plugin_catalog.models import PluginManifestV423

class PluginManifestLoaderV423:
    def __init__(self, root: str | Path | None = None):
        self.root = Path(root) if root else plugin_manifest_root()

    def list_files(self):
        if not self.root.exists():
            return []
        return sorted(self.root.glob("*.json"))

    def load_all(self):
        manifests = []
        for path in self.list_files():
            data = json.loads(path.read_text(encoding="utf-8"))
            manifests.append(PluginManifestV423(**data))
        return manifests

    def as_dict(self):
        return [m.model_dump() for m in self.load_all()]
