from app.platform_core.licensing.entitlements import entitlement_engine
def test_v500_alpha9_entitlement_resolve():
    r = entitlement_engine.resolve({"license_type": "pro"})
    assert r["ready"] is True
    assert r["features"]["ADVANCED_AI"] is True
