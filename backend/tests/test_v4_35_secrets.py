from app.platform_core.config_center.secrets import SecretReferenceRegistry

def test_v435_secrets():
    s = SecretReferenceRegistry()
    refs = s.seed_defaults()
    assert "EXCHANGE_API_KEY" in refs
    assert refs["EXCHANGE_API_KEY"]["exposed"] is False
