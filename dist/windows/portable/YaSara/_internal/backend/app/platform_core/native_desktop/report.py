from app.platform_core.native_desktop.backend_supervisor import desktop_backend_process_supervisor
from app.platform_core.native_desktop.dashboard_webview_host import dashboard_webview_host
from app.platform_core.native_desktop.entrypoint import native_desktop_entrypoint
from app.platform_core.native_desktop.health import native_desktop_health_service
from app.platform_core.native_desktop.main_window_host import native_main_window_host
from app.platform_core.native_desktop.safe_shutdown import desktop_safe_shutdown_controller
from app.platform_core.native_desktop.single_instance_guard import windows_single_instance_guard

class NativeDesktopApplicationReportService:
    def report(self):
        return {
            "ready": True,
            "build_id": "2026.49.A.001",
            "entrypoint": native_desktop_entrypoint.specification(),
            "main_window": native_main_window_host.configuration(),
            "backend_supervisor": desktop_backend_process_supervisor.policy(),
            "dashboard_webview": dashboard_webview_host.configuration(),
            "single_instance": windows_single_instance_guard.policy(),
            "safe_shutdown": desktop_safe_shutdown_controller.policy(),
            "health": native_desktop_health_service.health(),
            "final_exe_generated": False,
            "real_execution_enabled": False,
            "real_broker_connection_enabled": False,
            "commercial_execution_engine_enabled": False,
            "commercial_api_key_required": False,
        }

native_desktop_application_report_service = NativeDesktopApplicationReportService()
NativeDesktopApplicationReport = NativeDesktopApplicationReportService
native_desktop_application_report = native_desktop_application_report_service
