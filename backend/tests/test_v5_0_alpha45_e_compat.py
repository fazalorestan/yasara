from app.platform_core.production_runtime.enterprise.report import RuntimeEnterpriseReport, runtime_enterprise_report

def test_compat(): assert RuntimeEnterpriseReport().report()['ready'] and runtime_enterprise_report.report()['ready']
