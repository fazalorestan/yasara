from app.v500_alpha16_exchange_connector.models import ExchangeConnectorSummaryV500Alpha16
def test_v500_alpha16_summary():
    s = ExchangeConnectorSummaryV500Alpha16()
    assert s.ready is True
    assert s.default_exchange_count == 18
    assert s.real_exchange_connection is False
