class PatchScriptClassifier:
    def classify(self, script_name: str):
        name = script_name.lower()
        family = "v5" if name.startswith("apply_v5_") else "v4" if name.startswith("apply_v4_") else "v3" if name.startswith("apply_v3_") else "legacy"
        return {"script": script_name, "family": family, "is_router_patch": "router" in name or "auto_router" in name or "api_search" in name, "safe": script_name.startswith("apply_") and script_name.endswith(".py")}
patch_script_classifier = PatchScriptClassifier()
