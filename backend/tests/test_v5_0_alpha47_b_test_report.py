from app.platform_core.ci_pipeline.test_report import CITestReportService

def test_test_report(): assert CITestReportService().report()['ready'] is True
