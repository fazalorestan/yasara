from app.platform_core.exchanges.capabilities import ExchangeCapabilityMatrix
def test_v500_alpha16_capability_toobit():
    c = ExchangeCapabilityMatrix().seed_defaults()["toobit"]
    assert c["sandbox"] is True
    assert c["testnet"] is True
