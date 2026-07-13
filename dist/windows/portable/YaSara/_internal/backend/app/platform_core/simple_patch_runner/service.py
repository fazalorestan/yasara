from pathlib import Path
class SimplePatchRunnerService:
    def safe(self, name: str):
        lowered = name.lower()
        return name.startswith("apply_v") and name.endswith(".py") and not any(x in lowered for x in ["delete", "wipe", "drop", "remove_all", "format"])
    def discover_names(self, root: str):
        root_path = Path(root)
        result = []
        for folder in [root_path / "backend" / "scripts", root_path / "scripts"]:
            if folder.exists():
                for item in folder.glob("apply_v*.py"):
                    if item.is_file() and self.safe(item.name):
                        result.append(item.name)
        return sorted(set(result))
    def summary(self):
        return {"ready": True, "phase": "v5_0_alpha_33_1_simple_patch_runner_fix", "strategy": "direct_patch_function_rewrite_simple", "manual_router_patch_required_after_this": False, "backward_compatible": True}
simple_patch_runner_service = SimplePatchRunnerService()
