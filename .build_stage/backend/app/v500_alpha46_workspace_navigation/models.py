from pydantic import BaseModel

class WorkspaceNavigationSummaryV500Alpha46(BaseModel):
    ready: bool = True
    phase: str = "v5_0_alpha_46_desktop_foundation_package_c"
    scope: str = "workspace_navigation"
    workspace_manager: bool = True
    multi_workspace: bool = True
    dock_layout_manager: bool = True
    tab_manager: bool = True
    navigation_state_manager: bool = True
    command_palette_contract: bool = True
    shortcut_registry: bool = True
    window_state_persistence: bool = True
    hardcoded_dashboard: bool = False
    commercial_execution_engine_enabled: bool = False
    commercial_api_key_required: bool = False
    real_execution_enabled: bool = False
    real_broker_connection_enabled: bool = False
    backward_compatible: bool = True
    test_pack_size: int = 80
