from app.platform_core.windows_app.report import WindowsAppBootstrapReportService

def test_report(): assert WindowsAppBootstrapReportService().report()['ready'] is True
