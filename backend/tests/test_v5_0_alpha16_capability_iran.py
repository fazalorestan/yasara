from app.platform_core.exchanges.capabilities import ExchangeCapabilityMatrix
def test_v500_alpha16_capability_iran():
    c = ExchangeCapabilityMatrix().seed_defaults()["nobitex"]
    assert c["iran_market"] is True
    assert c["futures"] is False
