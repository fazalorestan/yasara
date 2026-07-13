from app.platform_core.production_runtime.startup_report import RuntimeStartupReportService

def test_report(): assert RuntimeStartupReportService().report()['ready'] is True
