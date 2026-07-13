class PluginHealthMonitor:
    def __init__(self):
        self._health = {}

    def set(self, plugin: str, state: str = "healthy", detail: str = ""):
        self._health[plugin] = {
            "plugin": plugin,
            "state": state,
            "detail": detail,
        }
        return self._health[plugin]

    def get(self, plugin: str):
        return self._health.get(plugin, {"plugin": plugin, "state": "unknown", "detail": ""})

    def list(self):
        return dict(self._health)

plugin_health_monitor = PluginHealthMonitor()
