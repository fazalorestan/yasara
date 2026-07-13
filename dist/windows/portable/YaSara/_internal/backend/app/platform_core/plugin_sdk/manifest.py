class PluginManifestService:
    def sample_manifest(self):
        return {
            "plugin_id": "demo.analytics",
            "name": "Demo Analytics Plugin",
            "version": "1.0.0",
            "api_version": "v1",
            "enabled": True,
            "capabilities": ["analytics", "reporting"],
            "metadata": {"vendor": "yasara", "sandbox_required": True},
        }

    def validate(self, manifest: dict):
        required = ["plugin_id", "name", "version", "api_version"]
        missing = [x for x in required if not manifest.get(x)]
        return {"ready": len(missing) == 0, "valid": len(missing) == 0, "missing": missing}

plugin_manifest_service = PluginManifestService()
