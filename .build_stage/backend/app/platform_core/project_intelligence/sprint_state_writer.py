from app.platform_core.project_intelligence.sprint_state import sprint_state_registry
from app.platform_core.project_intelligence.state_store import project_state_store

class SprintStateWriter:
    def write_sprint_state(self):
        sprint = sprint_state_registry.snapshot()
        return {
            "ready": True,
            "written": True,
            "current_sprint": sprint["current_sprint"],
            "current_package": sprint["current_package"],
            "next_package": sprint["next_package"],
            "store": project_state_store.base_state()["source"],
        }

sprint_state_writer = SprintStateWriter()
