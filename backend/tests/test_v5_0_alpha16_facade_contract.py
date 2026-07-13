from app.v500_alpha16_exchange_connector.service import ExchangeConnectorFacadeV500Alpha16
def test_v500_alpha16_facade_contract():
    c = ExchangeConnectorFacadeV500Alpha16().connector_contract()
    assert c["execution_allowed"] is False
