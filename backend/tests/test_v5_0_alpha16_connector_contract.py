from app.platform_core.exchanges.connector_contract import ExchangeConnectorContract
def test_v500_alpha16_connector_contract():
    c = ExchangeConnectorContract().contract()
    assert "connect" in c["required_methods"]
    assert c["real_connection_enabled"] is False
