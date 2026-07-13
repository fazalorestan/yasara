from app.platform_core.plugin_sdk.versioning_report import plugin_versioning_report_service

class PluginVersioningReadinessGate:
    def run(self):
        report = plugin_versioning_report_service.report()
        ready = report["ready"] and report["dependencies"]["valid"]
        return {"ready": ready, "checks": {"report_ready": report["ready"], "dependencies_valid": report["dependencies"]["valid"], "real_execution_allowed": False, "auto_trading_allowed": False}, "execution_allowed": False}

plugin_versioning_readiness_gate = PluginVersioningReadinessGate()
