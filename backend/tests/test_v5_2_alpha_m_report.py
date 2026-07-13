from app.platform_core.apscheduler_dependency_gate.report import APSchedulerDependencyGateReportService

def test_report(): assert APSchedulerDependencyGateReportService().report()['apscheduler_gate'] is True
