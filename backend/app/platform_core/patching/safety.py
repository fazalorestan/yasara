class PatchSafetyFilter:
    def allow(self, script_name: str):
        lowered = script_name.lower()
        denied = ["delete", "remove_all", "wipe", "drop"]
        return {"script": script_name, "allowed": script_name.startswith("apply_") and script_name.endswith(".py") and not any(x in lowered for x in denied)}
patch_safety_filter = PatchSafetyFilter()
