from app.cloud_v1.license import LicenseServiceV1, LicenseStateV1, LicenseTierV1

def test_license_pro_feature():
    assert LicenseServiceV1().can_use_feature(LicenseStateV1(tier=LicenseTierV1.PRO), "pro") is True
    assert LicenseServiceV1().can_use_feature(LicenseStateV1(tier=LicenseTierV1.FREE), "pro") is False
