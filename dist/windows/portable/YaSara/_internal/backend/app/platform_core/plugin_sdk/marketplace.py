class PluginMarketplaceMetadataService:
    def listing(self, manifest: dict):
        return {"ready": True, "plugin_id": manifest.get("plugin_id"), "name": manifest.get("name"), "version": manifest.get("version"), "category": "analytics", "verified": True, "commercial_allowed": False}

plugin_marketplace_metadata_service = PluginMarketplaceMetadataService()
