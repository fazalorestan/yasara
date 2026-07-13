from app.platform_core.desktop_app.command_palette import desktop_command_palette_contract
from app.platform_core.desktop_app.dock_layout_manager import desktop_dock_layout_manager
from app.platform_core.desktop_app.multi_workspace import desktop_multi_workspace_service
from app.platform_core.desktop_app.navigation_state import desktop_navigation_state_manager
from app.platform_core.desktop_app.shortcut_registry import desktop_shortcut_registry
from app.platform_core.desktop_app.tab_manager import desktop_tab_manager
from app.platform_core.desktop_app.window_state_persistence import desktop_window_state_persistence
from app.platform_core.desktop_app.workspace_manager import desktop_workspace_manager

class DesktopWorkspaceReportService:
    def report(self):
        return {
            "ready": True,
            "workspace": desktop_workspace_manager.workspace(),
            "multi_workspace": desktop_multi_workspace_service.support(),
            "dock_layout": desktop_dock_layout_manager.dock_layout(),
            "tabs": desktop_tab_manager.tabs(),
            "navigation_state": desktop_navigation_state_manager.state(),
            "command_palette": desktop_command_palette_contract.contract(),
            "shortcuts": desktop_shortcut_registry.shortcuts(),
            "window_state": desktop_window_state_persistence.state(),
            "hardcoded_dashboard": False,
            "real_execution_enabled": False,
            "real_broker_connection_enabled": False,
            "commercial_execution_engine_enabled": False,
            "commercial_api_key_required": False,
        }

desktop_workspace_report_service = DesktopWorkspaceReportService()
DesktopWorkspaceReport = DesktopWorkspaceReportService
desktop_workspace_report = desktop_workspace_report_service
