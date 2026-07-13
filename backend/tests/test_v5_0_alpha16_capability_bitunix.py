from app.platform_core.exchanges.capabilities import ExchangeCapabilityMatrix
def test_v500_alpha16_capability_bitunix():
    c = ExchangeCapabilityMatrix().seed_defaults()["bitunix"]
    assert c["spot"] is True
    assert c["futures"] is True
    assert c["websocket"] is True
