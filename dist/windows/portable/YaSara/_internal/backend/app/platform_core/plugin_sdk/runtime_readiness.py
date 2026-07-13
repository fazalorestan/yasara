from app.platform_core.plugin_sdk.runtime_report import plugin_runtime_report_service

class PluginRuntimeReadinessGate:
    def run(self):
        report = plugin_runtime_report_service.report()
        ready = report["ready"] and report["sandbox"]["allowed"] and report["permissions"]["allowed"]
        return {"ready": ready, "checks": {"report_ready": report["ready"], "sandbox_allowed": report["sandbox"]["allowed"], "permissions_allowed": report["permissions"]["allowed"], "real_execution_allowed": False, "auto_trading_allowed": False}, "execution_allowed": False}

plugin_runtime_readiness_gate = PluginRuntimeReadinessGate()
