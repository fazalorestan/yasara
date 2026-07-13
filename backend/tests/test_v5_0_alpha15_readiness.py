from app.platform_core.market_data.readiness import MarketDataReadinessGate
def test_v500_alpha15_readiness():
    r = MarketDataReadinessGate().run()
    assert r["ready"] is True
    assert r["checks"]["real_exchange_connection"] is False
