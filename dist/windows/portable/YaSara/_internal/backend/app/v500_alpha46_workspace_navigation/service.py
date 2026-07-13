from app.platform_core.desktop_app.command_palette import desktop_command_palette_contract
from app.platform_core.desktop_app.dock_layout_manager import desktop_dock_layout_manager
from app.platform_core.desktop_app.multi_workspace import desktop_multi_workspace_service
from app.platform_core.desktop_app.navigation_state import desktop_navigation_state_manager
from app.platform_core.desktop_app.shortcut_registry import desktop_shortcut_registry
from app.platform_core.desktop_app.tab_manager import desktop_tab_manager
from app.platform_core.desktop_app.window_state_persistence import desktop_window_state_persistence
from app.platform_core.desktop_app.workspace_manager import desktop_workspace_manager
from app.platform_core.desktop_app.workspace_readiness import desktop_workspace_readiness_gate
from app.platform_core.desktop_app.workspace_report import desktop_workspace_report_service
from app.v500_alpha46_workspace_navigation.models import WorkspaceNavigationSummaryV500Alpha46

class WorkspaceNavigationFacadeV500Alpha46:
    def summary(self): return WorkspaceNavigationSummaryV500Alpha46()
    def workspace(self): return desktop_workspace_manager.workspace()
    def multi_workspace(self): return desktop_multi_workspace_service.support()
    def dock_layout(self): return desktop_dock_layout_manager.dock_layout()
    def tabs(self): return desktop_tab_manager.tabs()
    def navigation_state(self): return desktop_navigation_state_manager.state()
    def command_palette(self): return desktop_command_palette_contract.contract()
    def shortcuts(self): return desktop_shortcut_registry.shortcuts()
    def window_state(self): return desktop_window_state_persistence.state()
    def report(self): return desktop_workspace_report_service.report()
    def readiness(self): return desktop_workspace_readiness_gate.run()
    def contract(self): return {"ready": True, "desktop_app": "package_c_workspace_navigation", "hardcoded_dashboard": False}

workspace_navigation_facade_v500_alpha46 = WorkspaceNavigationFacadeV500Alpha46()
