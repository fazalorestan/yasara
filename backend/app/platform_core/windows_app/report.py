from app.platform_core.windows_app.app_bootstrap import windows_app_bootstrap_service
from app.platform_core.windows_app.app_health import windows_app_health_service
from app.platform_core.windows_app.exe_handoff_readiness import windows_exe_handoff_readiness_contract
from app.platform_core.windows_app.live_dashboard_host import windows_live_dashboard_host
from app.platform_core.windows_app.local_backend_connector import windows_local_backend_connector
from app.platform_core.windows_app.main_window_contract import windows_main_window_contract
from app.platform_core.windows_app.runtime_shell import windows_runtime_shell_service
from app.platform_core.windows_app.startup_flow import windows_desktop_startup_flow

class WindowsAppBootstrapReportService:
    def report(self):
        return {
            "ready": True,
            "build_id": "2026.48.A.001",
            "bootstrap": windows_app_bootstrap_service.bootstrap(),
            "runtime_shell": windows_runtime_shell_service.shell(),
            "main_window": windows_main_window_contract.contract(),
            "startup_flow": windows_desktop_startup_flow.flow(),
            "local_backend": windows_local_backend_connector.connector(),
            "dashboard_host": windows_live_dashboard_host.host(),
            "health": windows_app_health_service.health(),
            "exe_handoff": windows_exe_handoff_readiness_contract.contract(),
            "exe_packaging_enabled": False,
            "hardcoded_dashboard": False,
            "real_execution_enabled": False,
            "real_broker_connection_enabled": False,
            "commercial_execution_engine_enabled": False,
            "commercial_api_key_required": False,
        }

windows_app_bootstrap_report_service = WindowsAppBootstrapReportService()
WindowsAppBootstrapReport = WindowsAppBootstrapReportService
windows_app_bootstrap_report = windows_app_bootstrap_report_service
