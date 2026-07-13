from app.platform_core.exchanges.sdk.capability_negotiation import ConnectorCapabilityNegotiator
def test_v500_alpha18_capability_negotiation_missing():
    r = ConnectorCapabilityNegotiator().negotiate("nobitex", ["futures"])
    assert r["ready"] is False
