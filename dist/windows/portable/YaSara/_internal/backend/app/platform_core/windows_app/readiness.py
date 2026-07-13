from app.platform_core.windows_app.report import windows_app_bootstrap_report_service

class WindowsAppBootstrapReadinessGate:
    def run(self):
        report = windows_app_bootstrap_report_service.report()
        ready = (
            report["ready"]
            and report["bootstrap"]["ready"]
            and report["runtime_shell"]["ready"]
            and report["main_window"]["ready"]
            and report["startup_flow"]["ready"]
            and report["local_backend"]["ready"]
            and report["dashboard_host"]["ready"]
            and report["health"]["crash_detected"] is False
            and report["health"]["auto_trading_enabled"] is False
            and report["hardcoded_dashboard"] is False
        )
        return {
            "ready": ready,
            "checks": {
                "bootstrap_ready": report["bootstrap"]["ready"],
                "runtime_shell_ready": report["runtime_shell"]["ready"],
                "main_window_ready": report["main_window"]["ready"],
                "local_backend_ready": report["local_backend"]["ready"],
                "dashboard_host_ready": report["dashboard_host"]["ready"],
                "signal_only_mode": report["health"]["signal_only_mode"],
                "auto_trading_enabled": report["health"]["auto_trading_enabled"],
                "exe_packaging_enabled": report["exe_packaging_enabled"],
                "hardcoded_dashboard": False,
                "real_execution_enabled": False,
                "real_broker_connection_enabled": False,
            },
        }

windows_app_bootstrap_readiness_gate = WindowsAppBootstrapReadinessGate()
