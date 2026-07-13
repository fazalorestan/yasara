from app.platform_core.project_intelligence.dashboard_data_provider import dashboard_data_provider
from app.platform_core.project_intelligence.dashboard_readiness import live_dashboard_readiness_gate
from app.platform_core.project_intelligence.dashboard_report import live_dashboard_report_service
from app.platform_core.project_intelligence.health_summary_view import health_summary_view_service
from app.platform_core.project_intelligence.module_summary_view import module_summary_view_service
from app.platform_core.project_intelligence.platform_progress_view import platform_progress_view_service
from app.platform_core.project_intelligence.progress_calculator import project_progress_calculator
from app.platform_core.project_intelligence.sprint_summary_view import sprint_summary_view_service
from app.platform_core.project_intelligence.test_summary_view import test_summary_view_service
from app.v500_alpha44_live_dashboard.models import LiveDashboardSummaryV500Alpha44
class LiveDashboardFacadeV500Alpha44:
    def summary(self): return LiveDashboardSummaryV500Alpha44()
    def data(self): return dashboard_data_provider.data()
    def progress(self): return project_progress_calculator.progress()
    def platform_progress(self): return platform_progress_view_service.view()
    def tests(self): return test_summary_view_service.view()
    def modules(self): return module_summary_view_service.view()
    def sprint(self): return sprint_summary_view_service.view()
    def health(self): return health_summary_view_service.view()
    def report(self): return live_dashboard_report_service.report()
    def readiness(self): return live_dashboard_readiness_gate.run()
    def contract(self): return {"ready": True, "project_intelligence": "package_b_live_dashboard_backend", "hardcoded_dashboard": False}
live_dashboard_facade_v500_alpha44 = LiveDashboardFacadeV500Alpha44()
