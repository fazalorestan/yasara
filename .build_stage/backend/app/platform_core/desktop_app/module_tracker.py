from app.platform_core.project_intelligence.module_summary_view import module_summary_view_service

class DesktopModuleTracker:
    def modules(self):
        modules = module_summary_view_service.view()
        return {
            "ready": True,
            "completed_modules": modules["completed_modules"],
            "active_modules": modules["active_modules"],
            "remaining_modules": modules["remaining_modules"],
            "completed_files": modules["completed_files"],
            "remaining_files": modules["remaining_files"],
            "source": modules["source"],
            "hardcoded_dashboard": False,
        }

desktop_module_tracker = DesktopModuleTracker()
