from app.platform_core.exchanges.sdk.base import BaseExchangeConnector
def test_v500_alpha18_base_connector():
    c = BaseExchangeConnector("binance")
    assert c.status()["real_connection"] is False
    assert c.initialize()["state"] == "initialized"
