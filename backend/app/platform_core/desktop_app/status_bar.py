class DesktopStatusBarService:
    def status_bar(self):
        return {
            "ready": True,
            "fields": ["version", "sprint", "tests", "health"],
            "live_status_enabled": True,
            "source": "project_intelligence_center",
            "hardcoded_dashboard": False,
        }

desktop_status_bar_service = DesktopStatusBarService()
