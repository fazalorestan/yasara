from app.platform_core.production_runtime.service_report import RuntimeServiceReportService

def test_report(): assert RuntimeServiceReportService().report()['ready'] is True
