from app.platform_core.enterprise_cache.models import RedisAdapterContract

class RedisAdapterContractService:
    def contract(self):
        return RedisAdapterContract().__dict__

redis_adapter_contract_service = RedisAdapterContractService()
