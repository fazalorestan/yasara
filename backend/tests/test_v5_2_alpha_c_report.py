from app.platform_core.windows_spec_fix.report import WindowsSpecOutputFixReportService

def test_report(): assert WindowsSpecOutputFixReportService().report()['ready'] is True
