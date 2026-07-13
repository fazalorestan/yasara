from app.platform_core.desktop_app.dashboard_intelligence_report import desktop_dashboard_intelligence_report_service

class DesktopDashboardIntelligenceReadinessGate:
    def run(self):
        report = desktop_dashboard_intelligence_report_service.report()
        ready = (
            report["ready"]
            and report["dashboard"]["ready"]
            and report["widgets"]["plugin_based"]
            and report["plugin_loader"]["plugin_loader_enabled"]
            and report["progress"]["ready"]
            and report["sprint"]["ready"]
            and report["modules"]["ready"]
            and report["tests"]["ready"]
            and report["build"]["ready"]
            and report["health"]["ready"]
            and report["hardcoded_dashboard"] is False
            and report["commercial_execution_engine_enabled"] is False
        )
        return {
            "ready": ready,
            "checks": {
                "dashboard_ready": report["dashboard"]["ready"],
                "widgets_plugin_based": report["widgets"]["plugin_based"],
                "plugin_loader_enabled": report["plugin_loader"]["plugin_loader_enabled"],
                "progress_ready": report["progress"]["ready"],
                "sprint_ready": report["sprint"]["ready"],
                "modules_ready": report["modules"]["ready"],
                "tests_ready": report["tests"]["ready"],
                "build_ready": report["build"]["ready"],
                "health_ready": report["health"]["ready"],
                "hardcoded_dashboard": False,
                "commercial_execution_engine_enabled": False,
                "commercial_api_key_required": False,
                "real_execution_enabled": False,
                "real_broker_connection_enabled": False,
            },
        }

desktop_dashboard_intelligence_readiness_gate = DesktopDashboardIntelligenceReadinessGate()
