from app.platform_core.plugin_sdk.manifest import plugin_manifest_service

class PluginRegistryService:
    def __init__(self):
        self._plugins = {}

    def register(self, manifest: dict):
        validation = plugin_manifest_service.validate(manifest)
        if not validation["valid"]:
            return {"ready": False, "registered": False, "reason": "invalid_manifest", "validation": validation}
        plugin_id = manifest["plugin_id"]
        self._plugins[plugin_id] = manifest
        return {"ready": True, "registered": True, "plugin_id": plugin_id}

    def list_plugins(self):
        return {"ready": True, "plugins": list(self._plugins.values()), "count": len(self._plugins)}

    def get(self, plugin_id: str):
        plugin = self._plugins.get(plugin_id)
        return {"ready": plugin is not None, "plugin": plugin}

plugin_registry_service = PluginRegistryService()
plugin_registry_service.register(plugin_manifest_service.sample_manifest())
