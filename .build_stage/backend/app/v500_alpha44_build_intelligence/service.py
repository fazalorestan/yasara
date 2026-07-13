from app.platform_core.project_intelligence.build_metadata import build_metadata_service
from app.platform_core.project_intelligence.build_state_writer import build_state_writer
from app.platform_core.project_intelligence.file_counter import project_file_counter
from app.platform_core.project_intelligence.sprint_state_writer import sprint_state_writer
from app.platform_core.project_intelligence.state_store import project_state_store
from app.platform_core.project_intelligence.state_sync_readiness import state_sync_readiness_gate
from app.platform_core.project_intelligence.state_sync_report import state_sync_report_service
from app.platform_core.project_intelligence.test_state_writer import test_state_writer
from app.v500_alpha44_build_intelligence.models import BuildIntelligenceSummaryV500Alpha44

class BuildIntelligenceFacadeV500Alpha44:
    def summary(self): return BuildIntelligenceSummaryV500Alpha44()
    def state_store(self): return project_state_store.base_state()
    def write_build_state(self): return build_state_writer.write_build_state()
    def write_test_state(self): return test_state_writer.write_test_state()
    def write_sprint_state(self): return sprint_state_writer.write_sprint_state()
    def file_count(self): return project_file_counter.count()
    def build_metadata(self): return build_metadata_service.metadata()
    def report(self): return state_sync_report_service.report()
    def readiness(self): return state_sync_readiness_gate.run()
    def contract(self): return {"ready": True, "project_intelligence": "package_c_build_intelligence", "hardcoded_dashboard": False}

build_intelligence_facade_v500_alpha44 = BuildIntelligenceFacadeV500Alpha44()
