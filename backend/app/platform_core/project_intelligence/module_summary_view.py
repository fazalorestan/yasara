from app.platform_core.project_intelligence.module_state import module_state_registry
class ModuleSummaryViewService:
    def view(self):
        m = module_state_registry.snapshot()
        return {"ready": True, "completed_modules": m["completed_modules"], "active_modules": m["active_modules"], "remaining_modules": m["remaining_modules"], "completed_files": m["completed_files"], "remaining_files": m["remaining_files"], "source": "module_state_registry"}
module_summary_view_service = ModuleSummaryViewService()
