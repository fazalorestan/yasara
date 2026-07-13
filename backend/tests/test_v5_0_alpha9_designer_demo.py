from app.platform_core.licensing.designer import license_designer_contract
def test_v500_alpha9_designer_demo():
    d = license_designer_contract.create_demo()
    assert d["payload"]["license_type"] == "demo"
    assert "signature" in d
