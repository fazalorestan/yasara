from app.platform_core.exchanges.sdk.lifecycle import ExchangeConnectorLifecycle
def test_v500_alpha18_lifecycle_states():
    states = ExchangeConnectorLifecycle().states()
    assert "connected" in states
    assert "shutdown" in states
