from app.platform_core.enterprise_storage.object_contract import ObjectStorageContractService

def test_v439_object_contract():
    c = ObjectStorageContractService().contract()
    assert c["enabled"] is False
    assert c["mode"] == "contract_only"
