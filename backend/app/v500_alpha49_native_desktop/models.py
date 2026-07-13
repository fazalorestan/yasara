from pydantic import BaseModel

class NativeDesktopApplicationSummaryV500Alpha49(BaseModel):
    ready: bool = True
    phase: str = "v5_0_alpha_49_package_a"
    scope: str = "native_desktop_application_host"
    build_id: str = "2026.49.A.001"
    desktop_entrypoint: bool = True
    main_window_host: bool = True
    backend_process_supervisor: bool = True
    dashboard_webview_host: bool = True
    single_instance_guard: bool = True
    safe_shutdown_controller: bool = True
    final_exe_generated: bool = False
    signal_only_mode: bool = True
    auto_trading_enabled: bool = False
    real_execution_enabled: bool = False
    real_broker_connection_enabled: bool = False
    commercial_execution_engine_enabled: bool = False
    commercial_api_key_required: bool = False
    backward_compatible: bool = True
    test_pack_size: int = 90
