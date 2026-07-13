from app.platform_core.diagnostics.models import DiagnosticCheck
from app.platform_core.kernel.plugin_registry import plugin_registry
from app.v424_plugin_registry_sync.sync import PluginRegistrySyncServiceV424

class PluginRegistryIntegrityCheck:
    def run(self):
        if len(plugin_registry.list()) == 0:
            PluginRegistrySyncServiceV424().sync()
        plugins = plugin_registry.list()
        invalid = [name for name, item in plugins.items() if not item.get("manifest") or not item.get("state")]
        return DiagnosticCheck(
            name="plugin_registry_integrity",
            ready=len(plugins) > 0 and len(invalid) == 0,
            severity="error" if invalid or not plugins else "info",
            detail=f"{len(plugins)} plugins in registry",
            data={"plugin_count": len(plugins), "invalid": invalid, "states": {k: v['state'] for k, v in plugins.items()}},
        )
