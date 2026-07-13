from app.platform_core.build_dashboard.report import build_dashboard_integration_report_service

class WindowsLiveDashboardHost:
    def host(self):
        report = build_dashboard_integration_report_service.report()
        return {
            "ready": True,
            "host": "windows_live_dashboard_host",
            "dashboard_ready": report["ready"],
            "build_id": report["build_id"],
            "quality_signal": report["quality_signal"]["signal"],
            "ci_signal": report["ci_signal"]["signal"],
            "release_signal": report["release_signal"]["signal"],
            "hardcoded_dashboard": False,
        }

windows_live_dashboard_host = WindowsLiveDashboardHost()
