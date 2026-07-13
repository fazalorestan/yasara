from app.platform_core.project_intelligence.state_sync_report import StateSyncReportService

def test_report(): assert StateSyncReportService().report()['dashboard_auto_update_ready'] is True
