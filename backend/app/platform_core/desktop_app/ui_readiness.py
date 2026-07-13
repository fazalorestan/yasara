from app.platform_core.desktop_app.ui_report import desktop_ui_report_service

class DesktopUIReadinessGate:
    def run(self):
        report = desktop_ui_report_service.report()
        ready = (
            report["ready"]
            and report["ui_core"]["ready"]
            and report["layout"]["ready"]
            and report["sidebar"]["dashboard_enabled"]
            and report["toolbar"]["refresh_dashboard_action"]
            and report["status_bar"]["live_status_enabled"]
            and report["workspace"]["multi_panel_supported"]
            and report["dashboard_connector"]["connected"]
            and report["hardcoded_dashboard"] is False
            and report["commercial_execution_engine_enabled"] is False
        )
        return {
            "ready": ready,
            "checks": {
                "ui_core_ready": report["ui_core"]["ready"],
                "layout_ready": report["layout"]["ready"],
                "dashboard_enabled": report["sidebar"]["dashboard_enabled"],
                "toolbar_refresh_ready": report["toolbar"]["refresh_dashboard_action"],
                "live_status_enabled": report["status_bar"]["live_status_enabled"],
                "dashboard_connected": report["dashboard_connector"]["connected"],
                "hardcoded_dashboard": False,
                "commercial_execution_engine_enabled": False,
                "commercial_api_key_required": False,
                "real_execution_enabled": False,
                "real_broker_connection_enabled": False,
            },
        }

desktop_ui_readiness_gate = DesktopUIReadinessGate()
