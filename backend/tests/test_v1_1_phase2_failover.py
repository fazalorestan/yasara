from app.v11_exchange_connectivity.failover import ExchangeFailoverRouterV11

def test_failover_router_preferred():
    router = ExchangeFailoverRouterV11()
    result = router.choose("bitunix")
    assert result.selected_exchange == "bitunix"
    assert result.fallback_used is False
