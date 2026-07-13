from app.platform_core.project_intelligence.health_state import project_health_state_registry
class HealthSummaryViewService:
    def view(self):
        h = project_health_state_registry.snapshot()
        return {"ready": True, "project_health": h["project_health"], "backward_compatibility": h["backward_compatibility"], "auto_router_registry": h["auto_router_registry"], "regression": h["regression"], "real_execution_enabled": h["real_execution_enabled"], "real_broker_connection_enabled": h["real_broker_connection_enabled"], "source": "health_state_registry"}
health_summary_view_service = HealthSummaryViewService()
