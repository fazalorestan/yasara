from app.platform_core.licensing.activation.expiry import LicenseExpiryChecker
def test_v500_alpha11_expiry_none():
    assert LicenseExpiryChecker().is_expired(None) is False
