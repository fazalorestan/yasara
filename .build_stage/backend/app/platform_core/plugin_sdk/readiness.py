from app.platform_core.plugin_sdk.service import plugin_sdk_core_service

class PluginSDKCoreReadinessGate:
    def run(self):
        status = plugin_sdk_core_service.status()
        registry = plugin_sdk_core_service.registry()
        loader = plugin_sdk_core_service.loader_contract()
        ready = status["ready"] and registry["ready"] and loader["ready"]
        return {
            "ready": ready,
            "checks": {
                "status_ready": status["ready"],
                "registry_ready": registry["ready"],
                "loader_ready": loader["ready"],
                "real_execution_allowed": False,
                "auto_trading_allowed": False,
            },
            "execution_allowed": False,
        }

plugin_sdk_core_readiness_gate = PluginSDKCoreReadinessGate()
