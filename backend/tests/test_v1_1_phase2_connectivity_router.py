from app.v11_exchange_connectivity.router import ExchangeConnectivityRouterV11

def test_connectivity_router_market_request():
    router = ExchangeConnectivityRouterV11()
    result = router.market_request("/api/v3/ticker/price", "binance")
    assert result["selected"]["selected_exchange"] == "binance"
    assert result["request"]["read_only"] is True
