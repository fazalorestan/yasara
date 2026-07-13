from app.v500_alpha11_license_activation.models import LicenseActivationSummaryV500Alpha11
def test_v500_alpha11_summary():
    s = LicenseActivationSummaryV500Alpha11()
    assert s.ready is True
    assert s.test_pack_size == 20
