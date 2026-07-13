from pathlib import Path

class PatchOrchestratorService:
    def discover(self, root: str):
        root_path = Path(root)
        folders = [root_path / "backend" / "scripts", root_path / "scripts"]
        scripts = []
        for folder in folders:
            if folder.exists():
                scripts.extend(p.name for p in folder.glob("apply_v*.py") if p.is_file())
        return sorted(set(scripts))

    def is_safe(self, script_name: str):
        lowered = script_name.lower()
        forbidden = ["delete", "wipe", "drop", "remove_all", "format"]
        return script_name.startswith("apply_v") and script_name.endswith(".py") and not any(x in lowered for x in forbidden)

    def summary(self):
        return {
            "ready": True,
            "phase": "v5_0_alpha_31_1_patch_orchestrator_hotfix",
            "manual_router_patch_required_after_this": False,
            "backward_compatible": True,
        }

patch_orchestrator_service = PatchOrchestratorService()
