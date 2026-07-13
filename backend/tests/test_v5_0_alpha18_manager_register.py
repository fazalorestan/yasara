from app.platform_core.exchanges.sdk.manager import ExchangeConnectorManager
def test_v500_alpha18_manager_register():
    m = ExchangeConnectorManager()
    assert m.register_connector("binance")["state"] == "registered"
