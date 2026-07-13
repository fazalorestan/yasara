from app.platform_core.project_intelligence.sprint_state import sprint_state_registry
class SprintSummaryViewService:
    def view(self):
        s = sprint_state_registry.snapshot()
        return {"ready": True, "current_sprint": s["current_sprint"], "current_package": s["current_package"], "next_package": s["next_package"], "source": "sprint_state_registry"}
sprint_summary_view_service = SprintSummaryViewService()
