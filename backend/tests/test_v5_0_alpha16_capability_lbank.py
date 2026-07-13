from app.platform_core.exchanges.capabilities import ExchangeCapabilityMatrix
def test_v500_alpha16_capability_lbank():
    c = ExchangeCapabilityMatrix().seed_defaults()["lbank"]
    assert c["spot"] is True
    assert c["futures"] is True
