from app.platform_core.production_runtime.service_report import RuntimeServiceReport, runtime_service_report

def test_compat(): assert RuntimeServiceReport().report()['ready'] and runtime_service_report.report()['ready']
