from app.v427_extension_host.models import ExtensionHostSummaryV427

def test_v427_summary():
    s = ExtensionHostSummaryV427()
    assert s.ready is True
    assert s.no_new_trading_features is True
    assert s.live_execution_enabled is False
