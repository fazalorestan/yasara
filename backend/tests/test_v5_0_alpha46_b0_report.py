from app.platform_core.stabilization.technical_debt_report import TechnicalDebtReportService

def test_report(): assert TechnicalDebtReportService().report()['technical_debt_status']=='controlled'
