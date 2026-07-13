from app.platform_core.licensing.ui.status_card import LicenseStatusCardContract
def test_v500_alpha13_status_card():
    r = LicenseStatusCardContract().build({"license_type": "demo"})
    assert r["ready"] is True
    assert r["badge"] == "DEMO"
