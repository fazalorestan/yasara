from app.platform_core.exchanges.readiness import ExchangeConnectorReadinessGate
def test_v500_alpha16_readiness():
    r = ExchangeConnectorReadinessGate().run()
    assert r["ready"] is True
    assert r["checks"]["bitunix_registered"] is True
