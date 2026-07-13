from app.platform_core.enterprise_storage.policies import StoragePolicyRegistry

def test_v439_policies():
    r = StoragePolicyRegistry()
    policies = r.seed_defaults()
    assert "artifacts" in policies
    assert "backups" in policies
