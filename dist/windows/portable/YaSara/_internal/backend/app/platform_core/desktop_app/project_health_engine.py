from app.platform_core.project_intelligence.health_summary_view import health_summary_view_service

class DesktopProjectHealthEngine:
    def health(self):
        health = health_summary_view_service.view()
        return {
            "ready": True,
            "project_health": health["project_health"],
            "backward_compatibility": health["backward_compatibility"],
            "auto_router_registry": health["auto_router_registry"],
            "regression": health["regression"],
            "real_execution_enabled": health["real_execution_enabled"],
            "real_broker_connection_enabled": health["real_broker_connection_enabled"],
            "source": health["source"],
            "hardcoded_dashboard": False,
        }

desktop_project_health_engine = DesktopProjectHealthEngine()
