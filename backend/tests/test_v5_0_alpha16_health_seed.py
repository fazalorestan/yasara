from app.platform_core.exchanges.health import ExchangeHealthMonitor
def test_v500_alpha16_health_seed():
    h = ExchangeHealthMonitor().seed_defaults(["binance", "bitunix"])
    assert h["binance"]["status"] == "disconnected"
