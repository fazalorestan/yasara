from app.platform_core.production_runtime.enterprise.report import RuntimeEnterpriseReportService

def test_report(): assert RuntimeEnterpriseReportService().report()['ready'] is True
