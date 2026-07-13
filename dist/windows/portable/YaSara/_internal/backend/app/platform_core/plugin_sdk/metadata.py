class PluginMetadataService:
    def metadata(self, manifest: dict):
        return {
            "ready": True,
            "plugin_id": manifest.get("plugin_id"),
            "vendor": manifest.get("metadata", {}).get("vendor", "unknown"),
            "license_required": bool(manifest.get("metadata", {}).get("license_required", False)),
            "sandbox_required": bool(manifest.get("metadata", {}).get("sandbox_required", True)),
        }

plugin_metadata_service = PluginMetadataService()
