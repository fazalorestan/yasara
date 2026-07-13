from app.platform_core.exchanges.sdk.base import BaseExchangeConnector
def test_v500_alpha18_base_connect_disconnect():
    c = BaseExchangeConnector("binance")
    assert c.connect()["state"] == "connected"
    assert c.disconnect()["state"] == "disconnected"
