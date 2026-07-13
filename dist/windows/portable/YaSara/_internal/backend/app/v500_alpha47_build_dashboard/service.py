from app.platform_core.build_dashboard.artifact_signal_provider import artifact_signal_provider
from app.platform_core.build_dashboard.build_timeline_provider import build_timeline_provider
from app.platform_core.build_dashboard.ci_signal_provider import ci_signal_provider
from app.platform_core.build_dashboard.integration_center import build_dashboard_integration_center
from app.platform_core.build_dashboard.pipeline_status_provider import pipeline_status_provider
from app.platform_core.build_dashboard.quality_signal_provider import build_quality_signal_provider
from app.platform_core.build_dashboard.readiness import build_dashboard_integration_readiness_gate
from app.platform_core.build_dashboard.release_signal_provider import release_signal_provider
from app.platform_core.build_dashboard.report import build_dashboard_integration_report_service
from app.v500_alpha47_build_dashboard.models import BuildDashboardSummaryV500Alpha47

class BuildDashboardFacadeV500Alpha47:
    def summary(self): return BuildDashboardSummaryV500Alpha47()
    def integration(self): return build_dashboard_integration_center.dashboard()
    def pipeline_status(self): return pipeline_status_provider.status()
    def build_timeline(self): return build_timeline_provider.timeline()
    def ci_signal(self): return ci_signal_provider.signal()
    def release_signal(self): return release_signal_provider.signal()
    def artifact_signal(self): return artifact_signal_provider.signal()
    def quality_signal(self): return build_quality_signal_provider.signal()
    def report(self): return build_dashboard_integration_report_service.report()
    def readiness(self): return build_dashboard_integration_readiness_gate.run()
    def contract(self): return {"ready": True, "build_dashboard": "package_d_pipeline_integration", "build_id": "2026.47.D.001"}

build_dashboard_facade_v500_alpha47 = BuildDashboardFacadeV500Alpha47()
