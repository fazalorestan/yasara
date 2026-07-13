from app.platform_core.project_intelligence.pic_report import project_intelligence_report_service
class ProjectIntelligenceReadinessGate:
    def run(self):
        r = project_intelligence_report_service.report()
        ready = all([r["ready"], r["project"]["ready"], r["sprint"]["ready"], r["version"]["ready"], r["build"]["ready"], r["tests"]["ready"], r["modules"]["ready"], r["health"]["ready"]])
        return {"ready": ready, "checks": {"project_state_ready": r["project"]["ready"], "sprint_state_ready": r["sprint"]["ready"], "version_state_ready": r["version"]["ready"], "build_state_ready": r["build"]["ready"], "test_state_ready": r["tests"]["ready"], "module_state_ready": r["modules"]["ready"], "health_state_ready": r["health"]["ready"], "hardcoded_dashboard": False}}
project_intelligence_readiness_gate = ProjectIntelligenceReadinessGate()
