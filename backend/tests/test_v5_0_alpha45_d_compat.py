from app.platform_core.production_runtime.diagnostics_report import RuntimeDiagnosticsReport, runtime_diagnostics_report

def test_compat(): assert RuntimeDiagnosticsReport().report()['ready'] and runtime_diagnostics_report.report()['ready']
