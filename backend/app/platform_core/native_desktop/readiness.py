from app.platform_core.native_desktop.report import native_desktop_application_report_service

class NativeDesktopApplicationReadinessGate:
    def run(self):
        r = native_desktop_application_report_service.report()
        ready = (
            r["ready"]
            and r["entrypoint"]["ready"]
            and r["main_window"]["ready"]
            and r["backend_supervisor"]["fail_closed"]
            and r["dashboard_webview"]["ready"]
            and r["single_instance"]["enabled"]
            and r["safe_shutdown"]["force_signal_only"]
            and r["health"]["auto_trading_enabled"] is False
        )
        return {
            "ready": ready,
            "checks": {
                "entrypoint_ready": r["entrypoint"]["ready"],
                "main_window_ready": r["main_window"]["ready"],
                "backend_fail_closed": r["backend_supervisor"]["fail_closed"],
                "dashboard_ready": r["dashboard_webview"]["ready"],
                "single_instance_enabled": r["single_instance"]["enabled"],
                "safe_shutdown_ready": r["safe_shutdown"]["ready"],
                "signal_only_mode": r["health"]["signal_only_mode"],
                "auto_trading_enabled": r["health"]["auto_trading_enabled"],
                "final_exe_generated": r["final_exe_generated"],
            },
        }

native_desktop_application_readiness_gate = NativeDesktopApplicationReadinessGate()
