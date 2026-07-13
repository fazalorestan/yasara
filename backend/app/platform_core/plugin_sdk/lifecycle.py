class PluginLifecycleService:
    def hooks(self):
        return {"ready": True, "hooks": ["on_load", "on_validate", "on_enable", "on_disable", "on_unload"]}

    def transition(self, state: str, event: str):
        table = {("created","load"):"loaded", ("loaded","enable"):"enabled", ("enabled","disable"):"disabled", ("disabled","unload"):"unloaded"}
        return {"ready": True, "from": state, "event": event, "to": table.get((state,event), state), "execution_allowed": False}

plugin_lifecycle_service = PluginLifecycleService()
