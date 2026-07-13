from pydantic import BaseModel

class LauncherSummaryV418(BaseModel):
    ready: bool = True
    phase: str = "v4_18_one_command_launcher_dashboard_auto_open"
    product_progress_percent: int = 80
    launcher_command: str = "python yasara.py start"
    dashboard_url: str = "http://127.0.0.1:5173"
    constitution_compliant: bool = True
    safety: str = "launcher_only_no_real_execution"
