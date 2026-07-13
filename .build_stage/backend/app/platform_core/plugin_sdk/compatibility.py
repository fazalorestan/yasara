class PluginCompatibilityService:
    def check(self, manifest: dict, supported_api_versions: list[str] | None = None):
        supported_api_versions = supported_api_versions or ["v1"]
        api_version = manifest.get("api_version")
        compatible = api_version in supported_api_versions
        return {
            "ready": True,
            "compatible": compatible,
            "api_version": api_version,
            "supported_api_versions": supported_api_versions,
        }

plugin_compatibility_service = PluginCompatibilityService()
