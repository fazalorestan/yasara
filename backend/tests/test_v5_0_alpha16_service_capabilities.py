from app.platform_core.exchanges.service import ExchangeConnectorFrameworkService
def test_v500_alpha16_service_capabilities():
    r = ExchangeConnectorFrameworkService().capabilities("toobit")
    assert r["capabilities"]["spot"] is True
