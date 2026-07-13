from app.v23_exchange_connector.service import ExchangeConnectorServiceV23

def test_exchange_connector_quote():
    q = ExchangeConnectorServiceV23().quote("BTC/USDT", "binance")
    assert q["ready"] is True
    assert q["symbol"] == "BTCUSDT"
    assert q["last"] > 0
    assert q["live_trading_enabled"] is False
