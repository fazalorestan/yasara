from app.platform_core.exchanges.sdk.readiness import ExchangeSDKReadinessGate
def test_v500_alpha18_readiness():
    r = ExchangeSDKReadinessGate().run()
    assert r["ready"] is True
    assert r["checks"]["real_connection_enabled"] is False
