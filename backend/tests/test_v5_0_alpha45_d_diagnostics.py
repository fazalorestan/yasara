from app.platform_core.production_runtime.runtime_diagnostics import RuntimeDiagnosticsService

def test_diagnostics(): assert RuntimeDiagnosticsService().diagnostics()['diagnostics_passed'] is True
