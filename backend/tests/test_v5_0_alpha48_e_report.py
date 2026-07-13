from app.platform_core.windows_builder.report import WindowsExecutableBuilderReportService

def test_report():
 assert WindowsExecutableBuilderReportService().report()['ready'] is True
