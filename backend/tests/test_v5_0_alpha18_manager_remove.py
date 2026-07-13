from app.platform_core.exchanges.sdk.manager import ExchangeConnectorManager
def test_v500_alpha18_manager_remove():
    m = ExchangeConnectorManager()
    m.register_connector("binance")
    assert m.remove_connector("binance")["removed"] is True
