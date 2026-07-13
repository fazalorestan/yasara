from app.platform_core.kernel.plugin_registry import PluginManifest, plugin_registry

class PluginLifecycleManager:
    def discover(self, manifest: PluginManifest): return plugin_registry.register(manifest, "discovered")
    def validate(self, name: str): return plugin_registry.set_state(name, "validated")
    def license(self, name: str): return plugin_registry.set_state(name, "licensed")
    def load(self, name: str): return plugin_registry.set_state(name, "loaded")
    def initialize(self, name: str): return plugin_registry.set_state(name, "initialized")
    def run(self, name: str): return plugin_registry.set_state(name, "running")
    def pause(self, name: str): return plugin_registry.set_state(name, "paused")
    def disable(self, name: str): return plugin_registry.set_state(name, "disabled")
    def unload(self, name: str): return plugin_registry.set_state(name, "unloaded")

plugin_lifecycle = PluginLifecycleManager()
