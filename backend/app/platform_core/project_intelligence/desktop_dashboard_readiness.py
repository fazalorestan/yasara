from app.platform_core.project_intelligence.desktop_dashboard_report import desktop_dashboard_report_service

class DesktopDashboardReadinessGate:
    def run(self):
        report = desktop_dashboard_report_service.report()
        ready = (
            report["ready"]
            and report["contract"]["ready"]
            and report["view_model"]["ready"]
            and report["layout"]["ready"]
            and report["widgets"]["ready"]
            and report["refresh"]["ready"]
            and report["hardcoded_dashboard"] is False
        )
        return {
            "ready": ready,
            "checks": {
                "contract_ready": report["contract"]["ready"],
                "view_model_ready": report["view_model"]["ready"],
                "layout_ready": report["layout"]["ready"],
                "widgets_ready": report["widgets"]["ready"],
                "refresh_ready": report["refresh"]["ready"],
                "desktop_shell_ready": report["desktop_shell_ready"],
                "exe_packaging_enabled": report["exe_packaging_enabled"],
                "hardcoded_dashboard": False,
            },
        }

desktop_dashboard_readiness_gate = DesktopDashboardReadinessGate()
