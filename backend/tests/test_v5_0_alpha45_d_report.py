from app.platform_core.production_runtime.diagnostics_report import RuntimeDiagnosticsReportService

def test_report(): assert RuntimeDiagnosticsReportService().report()['ready'] is True
