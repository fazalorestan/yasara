from app.v500_alpha13_license_ui.service import LicenseUIFacadeV500Alpha13
def test_v500_alpha13_facade_prompt():
    assert LicenseUIFacadeV500Alpha13().upgrade_prompt("AI_COACH")["recommended_plan"] == "elite"
