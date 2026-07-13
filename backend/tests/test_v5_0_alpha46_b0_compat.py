from app.platform_core.stabilization.technical_debt_report import TechnicalDebtReport, technical_debt_report

def test_compat(): assert TechnicalDebtReport().report()['ready'] and technical_debt_report.report()['ready']
