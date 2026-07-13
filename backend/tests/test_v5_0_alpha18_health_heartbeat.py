from app.platform_core.exchanges.sdk.health_watchdog import ExchangeConnectorHealthWatchdog
def test_v500_alpha18_health_heartbeat():
    r = ExchangeConnectorHealthWatchdog().heartbeat("binance", 10)
    assert r["metrics"]["heartbeat_count"] == 1
