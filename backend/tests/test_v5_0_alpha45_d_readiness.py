from app.platform_core.production_runtime.diagnostics_readiness import RuntimeDiagnosticsReadinessGate

def test_readiness(): assert RuntimeDiagnosticsReadinessGate().run()['ready'] is True
