from app.platform_core.project_intelligence.dashboard_layout_contract import dashboard_layout_contract_service
from app.platform_core.project_intelligence.dashboard_refresh_contract import dashboard_refresh_contract_service
from app.platform_core.project_intelligence.dashboard_view_model import dashboard_view_model_service
from app.platform_core.project_intelligence.dashboard_widget_contracts import dashboard_widget_contract_service
from app.platform_core.project_intelligence.desktop_dashboard_contract import desktop_dashboard_contract_service

class DesktopDashboardReportService:
    def report(self):
        return {
            "ready": True,
            "contract": desktop_dashboard_contract_service.contract(),
            "view_model": dashboard_view_model_service.view_model(),
            "layout": dashboard_layout_contract_service.layout(),
            "widgets": dashboard_widget_contract_service.widgets(),
            "refresh": dashboard_refresh_contract_service.refresh(),
            "desktop_shell_ready": True,
            "exe_packaging_enabled": False,
            "hardcoded_dashboard": False,
        }

desktop_dashboard_report_service = DesktopDashboardReportService()

# Backward Compatibility
DesktopDashboardReport = DesktopDashboardReportService
desktop_dashboard_report = desktop_dashboard_report_service
