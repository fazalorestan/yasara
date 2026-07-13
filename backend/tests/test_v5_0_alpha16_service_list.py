from app.platform_core.exchanges.service import ExchangeConnectorFrameworkService
def test_v500_alpha16_service_list():
    r = ExchangeConnectorFrameworkService().list_exchanges()
    assert r["ready"] is True
    assert "lbank" in r["exchanges"]
