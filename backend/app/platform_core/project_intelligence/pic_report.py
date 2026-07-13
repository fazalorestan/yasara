from app.platform_core.project_intelligence.build_state import build_state_registry
from app.platform_core.project_intelligence.health_state import project_health_state_registry
from app.platform_core.project_intelligence.module_state import module_state_registry
from app.platform_core.project_intelligence.project_state import project_state_registry
from app.platform_core.project_intelligence.sprint_state import sprint_state_registry
from app.platform_core.project_intelligence.test_state import test_state_registry
from app.platform_core.project_intelligence.version_state import version_state_registry

class ProjectIntelligenceReportService:
    def report(self):
        return {
            "ready": True,
            "project": project_state_registry.snapshot(),
            "sprint": sprint_state_registry.snapshot(),
            "version": version_state_registry.snapshot(),
            "build": build_state_registry.snapshot(),
            "tests": test_state_registry.snapshot(),
            "modules": module_state_registry.snapshot(),
            "health": project_health_state_registry.snapshot(),
            "dashboard_data_source": "project_state_registries",
            "hardcoded_dashboard": False,
        }
project_intelligence_report_service = ProjectIntelligenceReportService()
ProjectIntelligenceReport = ProjectIntelligenceReportService
project_intelligence_report = project_intelligence_report_service
