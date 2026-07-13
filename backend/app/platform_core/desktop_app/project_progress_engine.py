from app.platform_core.project_intelligence.progress_calculator import project_progress_calculator

class DesktopProjectProgressEngine:
    def progress(self):
        progress = project_progress_calculator.progress()
        return {
            "ready": True,
            "overall": progress["project_progress_percent"],
            "windows": progress["windows_progress_percent"],
            "android": progress["android_progress_percent"],
            "ios": progress["ios_progress_percent"],
            "web": progress["web_progress_percent"],
            "source": progress["source"],
            "hardcoded_dashboard": False,
        }

desktop_project_progress_engine = DesktopProjectProgressEngine()
