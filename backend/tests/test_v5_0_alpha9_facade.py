from app.v500_alpha9_license_core.service import LicenseCoreFacadeV500Alpha9
def test_v500_alpha9_facade():
    f = LicenseCoreFacadeV500Alpha9()
    assert f.summary().ready is True
    assert f.verify_demo()["ready"] is True
    assert f.can_access("BASIC_ANALYSIS", "demo")["enabled"] is True
