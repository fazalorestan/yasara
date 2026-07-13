from pydantic import BaseModel

class WindowsAppBootstrapSummaryV500Alpha48(BaseModel):
    ready: bool = True
    phase: str = "v5_0_alpha_48_package_a"
    scope: str = "windows_app_bootstrap_runtime_shell"
    build_id: str = "2026.48.A.001"
    windows_app_bootstrap: bool = True
    runtime_shell: bool = True
    main_window_contract: bool = True
    startup_flow: bool = True
    local_backend_connector: bool = True
    live_dashboard_host: bool = True
    windows_app_health: bool = True
    exe_handoff_readiness: bool = True
    exe_packaging_enabled: bool = False
    signal_only_mode: bool = True
    auto_trading_enabled: bool = False
    hardcoded_dashboard: bool = False
    commercial_execution_engine_enabled: bool = False
    commercial_api_key_required: bool = False
    real_execution_enabled: bool = False
    real_broker_connection_enabled: bool = False
    backward_compatible: bool = True
    test_pack_size: int = 90
