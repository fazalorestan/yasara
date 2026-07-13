from app.platform_core.enterprise_cache.policies import CachePolicyRegistry

def test_v438_policies():
    r = CachePolicyRegistry()
    policies = r.seed_defaults()
    assert "market_data" in policies
