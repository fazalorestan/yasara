from app.v430_platform_diagnostics.models import PlatformDiagnosticsSummaryV430

def test_v430_summary():
    s = PlatformDiagnosticsSummaryV430()
    assert s.ready is True
    assert s.no_new_trading_features is True
    assert s.live_execution_enabled is False
