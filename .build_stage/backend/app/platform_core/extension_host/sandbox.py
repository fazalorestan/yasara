from app.platform_core.extension_host.health_monitor import plugin_health_monitor
from app.platform_core.extension_host.models import PluginRuntimeInfo
from app.platform_core.extension_host.resource_quota import resource_quota_reporter
from app.platform_core.extension_host.startup_profiler import startup_profiler

class PluginSandbox:
    def __init__(self, plugin: str):
        self.plugin = plugin
        self.runtime = PluginRuntimeInfo(name=plugin)

    def start(self):
        self.runtime.state = "starting"
        startup_profiler.set(self.plugin, 0.0)
        self.runtime.state = "running"
        plugin_health_monitor.set(self.plugin, "healthy", "Sandbox started")
        resource_quota_reporter.set_quota(self.plugin)
        return self.status()

    def pause(self):
        self.runtime.state = "paused"
        plugin_health_monitor.set(self.plugin, "warning", "Sandbox paused")
        return self.status()

    def disable(self):
        self.runtime.state = "disabled"
        plugin_health_monitor.set(self.plugin, "disabled", "Sandbox disabled")
        return self.status()

    def stop(self):
        self.runtime.state = "stopped"
        plugin_health_monitor.set(self.plugin, "healthy", "Sandbox stopped")
        return self.status()

    def status(self):
        return {
            "plugin": self.plugin,
            "state": self.runtime.state,
            "health": plugin_health_monitor.get(self.plugin),
            "quota": resource_quota_reporter.report(self.plugin),
        }
