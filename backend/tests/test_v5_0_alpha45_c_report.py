from app.platform_core.production_runtime.lifecycle_report import RuntimeLifecycleReportService

def test_report(): assert RuntimeLifecycleReportService().report()['ready'] is True
