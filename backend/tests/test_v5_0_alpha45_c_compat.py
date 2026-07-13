from app.platform_core.production_runtime.lifecycle_report import RuntimeLifecycleReport, runtime_lifecycle_report

def test_compat(): assert RuntimeLifecycleReport().report()['ready'] and runtime_lifecycle_report.report()['ready']
