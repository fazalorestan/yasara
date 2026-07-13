from app.v500_alpha45_runtime_diagnostics.service import RuntimeDiagnosticsFacadeV500Alpha45

def test_commercial_no_execution(): assert RuntimeDiagnosticsFacadeV500Alpha45().report()['commercial_execution_engine_enabled'] is False
