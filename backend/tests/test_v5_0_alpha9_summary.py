from app.v500_alpha9_license_core.models import LicenseCoreSummaryV500Alpha9
def test_v500_alpha9_summary():
    s = LicenseCoreSummaryV500Alpha9()
    assert s.ready is True
    assert s.demo_days_default == 30
    assert s.test_pack_size == 20
