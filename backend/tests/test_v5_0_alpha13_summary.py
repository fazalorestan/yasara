from app.v500_alpha13_license_ui.models import LicenseUISummaryV500Alpha13
def test_v500_alpha13_summary():
    s = LicenseUISummaryV500Alpha13()
    assert s.ready is True
    assert s.test_pack_size == 20
