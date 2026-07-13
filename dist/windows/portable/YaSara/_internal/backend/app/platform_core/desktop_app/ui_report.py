from app.platform_core.desktop_app.layout_engine import desktop_layout_engine
from app.platform_core.desktop_app.live_dashboard_connector import desktop_live_dashboard_connector
from app.platform_core.desktop_app.notification_center import desktop_notification_center
from app.platform_core.desktop_app.sidebar_navigation import desktop_sidebar_navigation
from app.platform_core.desktop_app.status_bar import desktop_status_bar_service
from app.platform_core.desktop_app.toolbar_manager import desktop_toolbar_manager
from app.platform_core.desktop_app.ui_core import desktop_ui_core_service
from app.platform_core.desktop_app.workspace_panel import desktop_workspace_panel_contract

class DesktopUIReportService:
    def report(self):
        return {
            "ready": True,
            "ui_core": desktop_ui_core_service.status(),
            "layout": desktop_layout_engine.layout(),
            "sidebar": desktop_sidebar_navigation.sidebar(),
            "toolbar": desktop_toolbar_manager.toolbar(),
            "status_bar": desktop_status_bar_service.status_bar(),
            "notifications": desktop_notification_center.notifications(),
            "workspace": desktop_workspace_panel_contract.panel(),
            "dashboard_connector": desktop_live_dashboard_connector.connect(),
            "hardcoded_dashboard": False,
            "real_execution_enabled": False,
            "real_broker_connection_enabled": False,
            "commercial_execution_engine_enabled": False,
            "commercial_api_key_required": False,
        }

desktop_ui_report_service = DesktopUIReportService()
DesktopUIReport = DesktopUIReportService
desktop_ui_report = desktop_ui_report_service
