from app.v500_alpha10_license_enforcement.models import LicenseEnforcementSummaryV500Alpha10
def test_v500_alpha10_summary():
    s = LicenseEnforcementSummaryV500Alpha10()
    assert s.ready is True
    assert s.test_pack_size == 20
