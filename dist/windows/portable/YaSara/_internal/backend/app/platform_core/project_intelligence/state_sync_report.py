from app.platform_core.project_intelligence.build_metadata import build_metadata_service
from app.platform_core.project_intelligence.build_state_writer import build_state_writer
from app.platform_core.project_intelligence.file_counter import project_file_counter
from app.platform_core.project_intelligence.sprint_state_writer import sprint_state_writer
from app.platform_core.project_intelligence.state_store import project_state_store
from app.platform_core.project_intelligence.test_state_writer import test_state_writer

class StateSyncReportService:
    def report(self):
        return {
            "ready": True,
            "store": project_state_store.base_state(),
            "build_write": build_state_writer.write_build_state(),
            "test_write": test_state_writer.write_test_state(),
            "sprint_write": sprint_state_writer.write_sprint_state(),
            "file_count": project_file_counter.count(),
            "build_metadata": build_metadata_service.metadata(),
            "dashboard_auto_update_ready": True,
            "hardcoded_dashboard": False,
        }

state_sync_report_service = StateSyncReportService()

# Backward Compatibility
StateSyncReport = StateSyncReportService
state_sync_report = state_sync_report_service
