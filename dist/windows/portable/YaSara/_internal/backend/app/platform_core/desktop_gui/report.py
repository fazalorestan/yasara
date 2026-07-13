from app.platform_core.desktop_gui.build_panel import build_panel_contract
from app.platform_core.desktop_gui.ci_panel import ci_panel_contract
from app.platform_core.desktop_gui.dashboard_shell import desktop_dashboard_gui_shell
from app.platform_core.desktop_gui.health_panel import health_panel_contract
from app.platform_core.desktop_gui.navigation_shell import desktop_navigation_shell_contract
from app.platform_core.desktop_gui.runtime_panel import runtime_panel_contract
from app.platform_core.desktop_gui.status_bar import desktop_status_bar_contract
from app.platform_core.desktop_gui.ui_state import desktop_ui_state_contract

class DesktopDashboardGUIShellReportService:
    def report(self):
        return {
            "ready": True,
            "build_id": "2026.49.B.001",
            "shell": desktop_dashboard_gui_shell.shell(),
            "navigation": desktop_navigation_shell_contract.navigation(),
            "status_bar": desktop_status_bar_contract.status_bar(),
            "runtime_panel": runtime_panel_contract.panel(),
            "build_panel": build_panel_contract.panel(),
            "ci_panel": ci_panel_contract.panel(),
            "health_panel": health_panel_contract.panel(),
            "ui_state": desktop_ui_state_contract.state(),
            "final_exe_generated": False,
            "hardcoded_dashboard_data": False,
            "real_execution_enabled": False,
            "real_broker_connection_enabled": False,
            "commercial_execution_engine_enabled": False,
            "commercial_api_key_required": False,
        }

desktop_dashboard_gui_shell_report_service = DesktopDashboardGUIShellReportService()
DesktopDashboardGUIShellReport = DesktopDashboardGUIShellReportService
desktop_dashboard_gui_shell_report = desktop_dashboard_gui_shell_report_service
