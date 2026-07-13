from app.platform_core.production_readiness.report import ProductionReadinessReportService

def test_report(): assert ProductionReadinessReportService().report()['sprint_complete'] is True
