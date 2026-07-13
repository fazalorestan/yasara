from pathlib import Path
import re

class DefinitivePatchRunnerService:
    def version_key(self, name: str):
        m = re.search(r"apply_v(\d+)_(\d+)_alpha_(\d+)", name)
        if m:
            return (int(m.group(1)), int(m.group(2)), int(m.group(3)), name)
        m = re.search(r"apply_v(\d+)_(\d+)_(\d+)", name)
        if m:
            return (int(m.group(1)), int(m.group(2)), int(m.group(3)), name)
        return (0, 0, 0, name)

    def discover(self, root: str):
        root_path = Path(root)
        items = []
        for folder in [root_path / "backend" / "scripts", root_path / "scripts"]:
            if folder.exists():
                for p in folder.glob("apply_v*.py"):
                    if p.is_file() and self.safe(p.name):
                        items.append(p.name)
        return sorted(set(items), key=self.version_key)

    def safe(self, name: str):
        low = name.lower()
        return name.startswith("apply_v") and name.endswith(".py") and not any(x in low for x in ["delete", "wipe", "drop", "remove_all", "format"])

    def summary(self):
        return {"ready": True, "phase": "v5_0_alpha_32_1_definitive_patch_runner_hotfix", "manual_router_patch_required_after_this": False, "strategy": "direct_patch_function_rewrite"}

definitive_patch_runner_service = DefinitivePatchRunnerService()
