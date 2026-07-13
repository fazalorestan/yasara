from app.platform_core.project_intelligence.progress_calculator import project_progress_calculator
class PlatformProgressViewService:
    def view(self):
        p = project_progress_calculator.progress()
        return {"ready": True, "platforms": {"windows": p["windows_progress_percent"], "android": p["android_progress_percent"], "ios": p["ios_progress_percent"], "web": p["web_progress_percent"]}, "source": p["source"]}
platform_progress_view_service = PlatformProgressViewService()
