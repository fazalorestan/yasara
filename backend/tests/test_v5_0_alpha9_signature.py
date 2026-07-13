from app.platform_core.licensing.signature import license_signature_contract
def test_v500_alpha9_signature():
    payload = {"license_type": "demo"}
    sig = license_signature_contract.sign_demo(payload)
    assert license_signature_contract.verify_demo(payload, sig) is True
