from app.v23_exchange_connector.service import ExchangeConnectorServiceV23

def test_exchange_connector_capabilities():
    c = ExchangeConnectorServiceV23().capabilities()
    assert c["ready"] is True
    assert c["live_trading_enabled"] is False
    assert len(c["exchanges"]) >= 3
