from app.platform_core.project_intelligence.state_sync_report import StateSyncReport, state_sync_report

def test_compat(): assert StateSyncReport().report()['ready'] and state_sync_report.report()['ready']
