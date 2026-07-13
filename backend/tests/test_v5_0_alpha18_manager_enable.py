from app.platform_core.exchanges.sdk.manager import ExchangeConnectorManager
def test_v500_alpha18_manager_enable():
    m = ExchangeConnectorManager()
    assert m.enable_connector("binance")["state"] == "ready"
