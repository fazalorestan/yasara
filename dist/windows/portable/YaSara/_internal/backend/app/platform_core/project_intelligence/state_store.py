from datetime import datetime, timezone

class ProjectStateStore:
    def base_state(self):
        return {
            "ready": True,
            "updated_at": datetime.now(timezone.utc).isoformat(),
            "source": "project_state_store",
            "persistent_backend": "json_ready_contract",
            "real_execution_enabled": False,
            "real_broker_connection_enabled": False,
        }

    def write_stub(self, category: str):
        return {
            "ready": True,
            "category": category,
            "written": True,
            "durable": False,
            "mode": "contract_only",
        }

project_state_store = ProjectStateStore()
