from app.platform_core.project_intelligence.project_state import project_state_registry
class ProjectProgressCalculator:
    def progress(self):
        s = project_state_registry.snapshot()
        return {"ready": True, "project_progress_percent": s["project_progress_percent"], "windows_progress_percent": s["windows_progress_percent"], "android_progress_percent": s["android_progress_percent"], "ios_progress_percent": s["ios_progress_percent"], "web_progress_percent": s["web_progress_percent"], "source": "project_state_registry"}
project_progress_calculator = ProjectProgressCalculator()
