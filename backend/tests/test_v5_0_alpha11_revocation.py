from app.platform_core.licensing.activation.revocation import LicenseRevocationContract
def test_v500_alpha11_revocation():
    r = LicenseRevocationContract().revoke_plan("KEY")
    assert r["ready"] is True
    assert r["destructive"] is False
