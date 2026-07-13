from app.platform_core.desktop_gui.report import desktop_dashboard_gui_shell_report_service

class DesktopDashboardGUIShellReadinessGate:
    def run(self):
        r = desktop_dashboard_gui_shell_report_service.report()
        ready = (
            r["ready"]
            and r["shell"]["ready"]
            and r["navigation"]["ready"]
            and r["status_bar"]["ready"]
            and r["runtime_panel"]["ready"]
            and r["build_panel"]["ready"]
            and r["ci_panel"]["tests_failed"] == 0
            and r["health_panel"]["quality_signal"] == "green"
            and r["hardcoded_dashboard_data"] is False
        )
        return {
            "ready": ready,
            "checks": {
                "shell_ready": r["shell"]["ready"],
                "navigation_ready": r["navigation"]["ready"],
                "status_bar_ready": r["status_bar"]["ready"],
                "runtime_panel_ready": r["runtime_panel"]["ready"],
                "build_panel_ready": r["build_panel"]["ready"],
                "ci_tests_failed": r["ci_panel"]["tests_failed"],
                "quality_signal": r["health_panel"]["quality_signal"],
                "hardcoded_dashboard_data": False,
                "final_exe_generated": r["final_exe_generated"],
            },
        }

desktop_dashboard_gui_shell_readiness_gate = DesktopDashboardGUIShellReadinessGate()
