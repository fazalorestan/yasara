from app.platform_core.exchanges.sdk.events import ExchangeConnectorEventPublisher
def test_v500_alpha18_events():
    e = ExchangeConnectorEventPublisher()
    assert "ConnectorReady" in e.supported_events()
    assert e.publish("ConnectorReady", "binance")["ready"] is True
