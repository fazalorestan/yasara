from app.platform_core.in_process_backend_runner.report import InProcessBackendRunnerReportService

def test_report(): assert InProcessBackendRunnerReportService().report()['ready'] is True
