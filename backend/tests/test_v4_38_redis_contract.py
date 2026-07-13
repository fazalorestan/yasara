from app.platform_core.enterprise_cache.redis_contract import RedisAdapterContractService

def test_v438_redis_contract():
    c = RedisAdapterContractService().contract()
    assert c["enabled"] is False
    assert c["mode"] == "contract_only"
