class PluginHealthService:
    def health(self, manifest: dict):
        return {"ready": True, "plugin_id": manifest.get("plugin_id"), "status": "ok", "sandboxed": True, "execution_allowed": False}

plugin_health_service = PluginHealthService()
