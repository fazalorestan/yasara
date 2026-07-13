from app.v23_exchange_connector.service import ExchangeConnectorServiceV23

def test_exchange_connector_orderbook():
    ob = ExchangeConnectorServiceV23().orderbook("BTCUSDT", "binance")
    assert ob["ready"] is True
    assert len(ob["asks"]) == 7
    assert len(ob["bids"]) == 7
