from app.v23_exchange_connector.service import ExchangeConnectorServiceV23

def test_exchange_connector_ohlc():
    o = ExchangeConnectorServiceV23().ohlc_live_ready("BTCUSDT", "binance", "4H", 30)
    assert o["ready"] is True
    assert len(o["candles"]) == 30
    assert o["source"] == "v23_exchange_connector_ohlc"
