from app.v500_alpha12_license_manager.models import LicenseManagerSummaryV500Alpha12
def test_v500_alpha12_summary():
    s = LicenseManagerSummaryV500Alpha12()
    assert s.ready is True
    assert s.test_pack_size == 20
