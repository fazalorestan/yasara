from app.v425_policy_gate.models import PolicyGateSummaryV425

def test_v425_summary():
    s = PolicyGateSummaryV425()
    assert s.ready is True
    assert s.no_new_trading_features is True
    assert s.live_execution_enabled is False
