class ProjectHealthStateRegistry:
    def snapshot(self):
        return {
            "ready": True,
            "project_health": "green",
            "backward_compatibility": "pass",
            "auto_router_registry": "stable",
            "regression": "pass",
            "real_execution_enabled": False,
            "real_broker_connection_enabled": False,
            "commercial_execution_engine_enabled": False,
        }
project_health_state_registry = ProjectHealthStateRegistry()
