from app.v500_alpha45_runtime_diagnostics.service import RuntimeDiagnosticsFacadeV500Alpha45

def test_no_real_execution(): assert RuntimeDiagnosticsFacadeV500Alpha45().report()['real_execution_enabled'] is False
