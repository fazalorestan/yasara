from app.platform_core.production_readiness.technical_debt_control import ProductionTechnicalDebtControlService

def test_debt(): assert ProductionTechnicalDebtControlService().report()['refactor_debt_blocking_windows_exe'] is False
