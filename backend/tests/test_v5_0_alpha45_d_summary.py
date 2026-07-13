from app.v500_alpha45_runtime_diagnostics.models import RuntimeDiagnosticsSummaryV500Alpha45

def test_summary():
 s=RuntimeDiagnosticsSummaryV500Alpha45(); assert s.ready and s.test_pack_size==80 and s.commercial_execution_engine_enabled is False
