from app.platform_core.contracts.base import BaseContract

class StorageContract(BaseContract):
    contract_name = "storage"

    def write(self, key: str, payload: dict):
        raise NotImplementedError("Storage plugins must implement write(key, payload)")
