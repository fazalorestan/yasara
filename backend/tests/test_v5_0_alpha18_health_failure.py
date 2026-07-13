from app.platform_core.exchanges.sdk.health_watchdog import ExchangeConnectorHealthWatchdog
def test_v500_alpha18_health_failure():
    r = ExchangeConnectorHealthWatchdog().record_failure("binance", "x")
    assert r["metrics"]["failure_count"] == 1
