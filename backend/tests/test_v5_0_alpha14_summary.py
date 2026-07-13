from app.v500_alpha14_license_readiness.models import LicenseFinalReadinessSummaryV500Alpha14
def test_v500_alpha14_summary():
    s = LicenseFinalReadinessSummaryV500Alpha14()
    assert s.ready is True
    assert s.subsystem == "license_entitlement"
    assert s.test_pack_size == 20
