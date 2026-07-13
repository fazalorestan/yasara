class SelfHealingPatchSafety:
    def validate(self, script_name: str):
        low = script_name.lower()
        forbidden = ["delete","drop","wipe","remove_all","format"]
        allowed = script_name.startswith("apply_v") and script_name.endswith(".py") and not any(x in low for x in forbidden)
        return {"ready": True, "script": script_name, "allowed": allowed}
self_healing_patch_safety = SelfHealingPatchSafety()
