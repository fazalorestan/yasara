from app.v500_alpha14_license_readiness.service import LicenseFinalReadinessFacadeV500Alpha14
def test_v500_alpha14_facade_handoff():
    assert LicenseFinalReadinessFacadeV500Alpha14().handoff()["ready"] is True
