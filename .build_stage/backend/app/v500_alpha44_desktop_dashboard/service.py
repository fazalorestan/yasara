from app.platform_core.project_intelligence.dashboard_layout_contract import dashboard_layout_contract_service
from app.platform_core.project_intelligence.dashboard_refresh_contract import dashboard_refresh_contract_service
from app.platform_core.project_intelligence.dashboard_view_model import dashboard_view_model_service
from app.platform_core.project_intelligence.dashboard_widget_contracts import dashboard_widget_contract_service
from app.platform_core.project_intelligence.desktop_dashboard_contract import desktop_dashboard_contract_service
from app.platform_core.project_intelligence.desktop_dashboard_readiness import desktop_dashboard_readiness_gate
from app.platform_core.project_intelligence.desktop_dashboard_report import desktop_dashboard_report_service
from app.v500_alpha44_desktop_dashboard.models import DesktopDashboardSummaryV500Alpha44

class DesktopDashboardFacadeV500Alpha44:
    def summary(self): return DesktopDashboardSummaryV500Alpha44()
    def contract(self): return desktop_dashboard_contract_service.contract()
    def view_model(self): return dashboard_view_model_service.view_model()
    def layout(self): return dashboard_layout_contract_service.layout()
    def widgets(self): return dashboard_widget_contract_service.widgets()
    def refresh(self): return dashboard_refresh_contract_service.refresh()
    def report(self): return desktop_dashboard_report_service.report()
    def readiness(self): return desktop_dashboard_readiness_gate.run()
    def api_contract(self): return {"ready": True, "project_intelligence": "package_d_desktop_dashboard_shell", "hardcoded_dashboard": False}

desktop_dashboard_facade_v500_alpha44 = DesktopDashboardFacadeV500Alpha44()
