from app.platform_core.plugin_sdk.health import plugin_health_service
from app.platform_core.plugin_sdk.lifecycle import plugin_lifecycle_service
from app.platform_core.plugin_sdk.manifest import plugin_manifest_service
from app.platform_core.plugin_sdk.permissions import plugin_permission_gate
from app.platform_core.plugin_sdk.runtime import plugin_runtime_service
from app.platform_core.plugin_sdk.sandbox import plugin_sandbox_policy

class PluginRuntimeReportService:
    def report(self):
        manifest = plugin_manifest_service.sample_manifest()
        return {"ready": True, "manifest": manifest, "runtime": plugin_runtime_service.runtime_context(manifest), "sandbox": plugin_sandbox_policy.evaluate(manifest), "permissions": plugin_permission_gate.check(manifest), "lifecycle": plugin_lifecycle_service.hooks(), "health": plugin_health_service.health(manifest), "execution_allowed": False}

plugin_runtime_report_service = PluginRuntimeReportService()
