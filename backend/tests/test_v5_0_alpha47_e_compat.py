from app.platform_core.production_readiness.report import ProductionReadinessReport, production_readiness_report

def test_compat(): assert ProductionReadinessReport().report()['ready'] and production_readiness_report.report()['ready']
