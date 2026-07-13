from app.v11_exchange_connectivity.health import ExchangeConnectivityHealthServiceV11

def test_exchange_health_all():
    health = ExchangeConnectivityHealthServiceV11().check_all()
    assert len(health) == 3
    assert all(h.state.value == "healthy" for h in health)
