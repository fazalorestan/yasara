from app.v11_exchange_connectivity.service import ExchangeConnectivityServiceV11

def test_service_diagnostics():
    diagnostics = ExchangeConnectivityServiceV11().diagnostics()
    assert diagnostics["summary"]["ready"] is True
    assert diagnostics["summary"]["live_trading_enabled"] is False
