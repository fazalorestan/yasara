from app.platform_core.licensing.manager.plans import LicensePlanBuilder
def test_v500_alpha12_plan_demo():
    r = LicensePlanBuilder().build("demo", 30)
    assert r["device_limit"] == 1
    assert "BASIC_ANALYSIS" in r["features"]
