from app.v23_exchange_connector.service import ExchangeConnectorServiceV23

def test_exchange_connector_summary():
    s = ExchangeConnectorServiceV23().summary()
    assert s.operational_progress_percent == 85
    assert s.remaining_to_full_operational_percent == 15
