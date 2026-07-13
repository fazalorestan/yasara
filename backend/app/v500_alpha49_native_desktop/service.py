from app.platform_core.native_desktop.backend_supervisor import desktop_backend_process_supervisor
from app.platform_core.native_desktop.dashboard_webview_host import dashboard_webview_host
from app.platform_core.native_desktop.entrypoint import native_desktop_entrypoint
from app.platform_core.native_desktop.health import native_desktop_health_service
from app.platform_core.native_desktop.main_window_host import native_main_window_host
from app.platform_core.native_desktop.readiness import native_desktop_application_readiness_gate
from app.platform_core.native_desktop.report import native_desktop_application_report_service
from app.platform_core.native_desktop.safe_shutdown import desktop_safe_shutdown_controller
from app.platform_core.native_desktop.single_instance_guard import windows_single_instance_guard
from app.v500_alpha49_native_desktop.models import NativeDesktopApplicationSummaryV500Alpha49

class NativeDesktopApplicationFacadeV500Alpha49:
    def summary(self): return NativeDesktopApplicationSummaryV500Alpha49()
    def entrypoint(self): return native_desktop_entrypoint.specification()
    def main_window(self): return native_main_window_host.configuration()
    def backend_supervisor(self): return desktop_backend_process_supervisor.policy()
    def dashboard_webview(self): return dashboard_webview_host.configuration()
    def single_instance(self): return windows_single_instance_guard.policy()
    def safe_shutdown(self): return desktop_safe_shutdown_controller.policy()
    def health(self): return native_desktop_health_service.health()
    def report(self): return native_desktop_application_report_service.report()
    def readiness(self): return native_desktop_application_readiness_gate.run()
    def contract(self): return {"ready": True, "native_desktop": "package_a_application_host", "build_id": "2026.49.A.001"}

native_desktop_application_facade_v500_alpha49 = NativeDesktopApplicationFacadeV500Alpha49()
