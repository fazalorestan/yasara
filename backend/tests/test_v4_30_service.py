from app.v430_platform_diagnostics.service import PlatformDiagnosticsServiceV430

def test_v430_service():
    s = PlatformDiagnosticsServiceV430()
    assert s.summary().ready is True
    assert s.readiness()["ready"] is True
    assert s.paths()["ready"] is True
