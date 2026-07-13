from app.platform_core.desktop_launcher.report import desktop_runtime_launcher_report_service

class DesktopRuntimeLauncherReadinessGate:
    def run(self):
        r = desktop_runtime_launcher_report_service.report()
        ready = (
            r["ready"]
            and r["runtime_launcher"]["ready"]
            and r["backend_launch"]["ready"]
            and r["backend_launch"]["fail_closed_on_error"]
            and r["dashboard_launch"]["ready"]
            and r["launch_flow"]["signal_only_default"]
            and r["launch_flow"]["auto_trading_enabled_default"] is False
            and r["smoke_test"]["smoke_test_passed"]
            and r["launch_health"]["launch_health"] == "green"
        )
        return {
            "ready": ready,
            "checks": {
                "runtime_launcher_ready": r["runtime_launcher"]["ready"],
                "backend_launch_ready": r["backend_launch"]["ready"],
                "dashboard_launch_ready": r["dashboard_launch"]["ready"],
                "smoke_test_passed": r["smoke_test"]["smoke_test_passed"],
                "launch_health": r["launch_health"]["launch_health"],
                "signal_only_mode": r["launch_health"]["signal_only_mode"],
                "auto_trading_enabled": r["launch_health"]["auto_trading_enabled"],
                "final_exe_generated": r["final_exe_generated"],
            },
        }

desktop_runtime_launcher_readiness_gate = DesktopRuntimeLauncherReadinessGate()
