from app.platform_core.licensing.entitlements import entitlement_engine
def test_v500_alpha9_can_access():
    r = entitlement_engine.can_access({"license_type": "demo"}, "EXPORT")
    assert r["enabled"] is False
