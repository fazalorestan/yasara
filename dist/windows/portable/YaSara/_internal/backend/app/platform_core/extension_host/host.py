from app.platform_core.extension_host.dependency_graph import plugin_dependency_graph
from app.platform_core.extension_host.health_monitor import plugin_health_monitor
from app.platform_core.extension_host.recovery import recovery_manager
from app.platform_core.extension_host.sandbox import PluginSandbox
from app.platform_core.extension_host.shutdown import safe_shutdown_contract
from app.platform_core.extension_host.startup_profiler import startup_profiler
from app.v423_plugin_catalog.loader import PluginManifestLoaderV423

class ExtensionHost:
    def __init__(self):
        self._sandboxes = {}
        self.loader = PluginManifestLoaderV423()

    def load_catalog(self):
        manifests = self.loader.load_all()
        plugin_dependency_graph.build(manifests)
        for m in manifests:
            self._sandboxes.setdefault(m.name, PluginSandbox(m.name))
        return {
            "ready": True,
            "plugin_count": len(self._sandboxes),
            "plugins": sorted(self._sandboxes.keys()),
            "dependency_graph": plugin_dependency_graph.report(),
            "mode": "report_only",
        }

    def start_all(self):
        self.load_catalog()
        results = []
        for name, sandbox in self._sandboxes.items():
            results.append(startup_profiler.measure(name, sandbox.start))
        return {
            "ready": True,
            "started_count": len(results),
            "results": results,
            "startup": startup_profiler.report(),
            "mode": "report_only",
        }

    def health(self):
        self.load_catalog()
        for name in self._sandboxes:
            plugin_health_monitor.set(name, "healthy", "Registered in Extension Host")
        return {
            "ready": True,
            "health": plugin_health_monitor.list(),
        }

    def shutdown_plan(self, plugin: str):
        return safe_shutdown_contract.plan(plugin)

    def recover(self, plugin: str, error: str = ""):
        return recovery_manager.recover(plugin, error)

extension_host = ExtensionHost()
