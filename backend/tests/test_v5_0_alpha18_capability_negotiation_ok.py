from app.platform_core.exchanges.sdk.capability_negotiation import ConnectorCapabilityNegotiator
def test_v500_alpha18_capability_negotiation_ok():
    r = ConnectorCapabilityNegotiator().negotiate("binance", ["spot", "rest"])
    assert r["ready"] is True
