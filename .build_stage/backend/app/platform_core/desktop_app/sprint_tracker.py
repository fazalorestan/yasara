from app.platform_core.project_intelligence.sprint_summary_view import sprint_summary_view_service

class DesktopSprintTracker:
    def sprint(self):
        sprint = sprint_summary_view_service.view()
        return {
            "ready": True,
            "current_sprint": sprint["current_sprint"],
            "current_package": sprint["current_package"],
            "next_package": sprint["next_package"],
            "source": sprint["source"],
            "hardcoded_dashboard": False,
        }

desktop_sprint_tracker = DesktopSprintTracker()
