from app.platform_core.licensing.designer import license_designer_contract
def test_v500_alpha9_designer_contract():
    c = license_designer_contract.design_contract()
    assert c["signed_payload_required"] is True
    assert 14 in c["duration_options"]
