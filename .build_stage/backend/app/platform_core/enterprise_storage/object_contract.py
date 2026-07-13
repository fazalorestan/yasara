from app.platform_core.enterprise_storage.models import ObjectStorageContract

class ObjectStorageContractService:
    def contract(self):
        return ObjectStorageContract().__dict__

object_storage_contract_service = ObjectStorageContractService()
