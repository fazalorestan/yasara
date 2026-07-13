from app.platform_core.licensing.manager.plans import LicensePlanBuilder
def test_v500_alpha12_plan_enterprise():
    r = LicensePlanBuilder().build("enterprise", 365)
    assert r["device_limit"] == 10
    assert "IRAN_MARKET" in r["features"]
