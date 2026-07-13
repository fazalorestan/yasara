from app.platform_core.production_runtime.startup_report import RuntimeStartupReport, runtime_startup_report

def test_compat(): assert RuntimeStartupReport().report()['ready'] and runtime_startup_report.report()['ready']
