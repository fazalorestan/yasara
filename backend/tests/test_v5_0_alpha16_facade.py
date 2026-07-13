from app.v500_alpha16_exchange_connector.service import ExchangeConnectorFacadeV500Alpha16
def test_v500_alpha16_facade():
    f = ExchangeConnectorFacadeV500Alpha16()
    assert f.summary().ready is True
    assert f.readiness()["ready"] is True
