from app.platform_core.exchanges.service import ExchangeConnectorFrameworkService
def test_v500_alpha16_service_metadata():
    r = ExchangeConnectorFrameworkService().metadata("bitunix")
    assert r["metadata"]["exchange_id"] == "bitunix"
