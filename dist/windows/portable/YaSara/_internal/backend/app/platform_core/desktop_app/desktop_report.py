from app.platform_core.desktop_app.config_loader import desktop_config_loader
from app.platform_core.desktop_app.desktop_bootstrap import desktop_bootstrap_service
from app.platform_core.desktop_app.desktop_health import desktop_health_contract
from app.platform_core.desktop_app.desktop_host import desktop_host_service
from app.platform_core.desktop_app.desktop_session import desktop_session_manager
from app.platform_core.desktop_app.navigation_shell import desktop_navigation_shell
from app.platform_core.desktop_app.theme_manager import desktop_theme_manager
from app.platform_core.desktop_app.window_manager import desktop_window_manager
class DesktopHostReportService:
    def report(self):
        return {"ready": True, "host": desktop_host_service.status(), "bootstrap": desktop_bootstrap_service.bootstrap(), "window": desktop_window_manager.window(), "navigation": desktop_navigation_shell.navigation(), "theme": desktop_theme_manager.theme(), "config": desktop_config_loader.config(), "session": desktop_session_manager.session(), "health": desktop_health_contract.health(), "exe_packaging_enabled": False, "hardcoded_dashboard": False, "real_execution_enabled": False, "real_broker_connection_enabled": False, "commercial_execution_engine_enabled": False, "commercial_api_key_required": False}
desktop_host_report_service = DesktopHostReportService()
DesktopHostReport = DesktopHostReportService
desktop_host_report = desktop_host_report_service
