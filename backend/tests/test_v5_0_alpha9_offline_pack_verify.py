from app.platform_core.licensing.offline import offline_license_contract
def test_v500_alpha9_offline_pack_verify():
    blob = offline_license_contract.pack({"license_type": "demo"})
    assert offline_license_contract.verify(blob)["ready"] is True
