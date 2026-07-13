from app.platform_core.exchanges.health import ExchangeHealthMonitor
def test_v500_alpha16_health_set():
    h = ExchangeHealthMonitor()
    assert h.set_status("binance", "connected")["status"] == "connected"
