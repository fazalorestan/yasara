from app.platform_core.exchanges.sdk.lifecycle import ExchangeConnectorLifecycle
def test_v500_alpha18_lifecycle_transition():
    l = ExchangeConnectorLifecycle()
    assert l.can_transition("discovered", "registered") is True
    assert l.can_transition("shutdown", "connected") is False
