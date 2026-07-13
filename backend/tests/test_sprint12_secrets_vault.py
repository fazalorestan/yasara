import pytest
from app.secrets_v1.application.service import SecretsVaultServiceV1
from app.secrets_v1.domain.models import SecretCreateRequest, SecretScope

@pytest.mark.asyncio
async def test_secret_encrypt_resolve_without_leak():
    service = SecretsVaultServiceV1()
    public = await service.create_secret(SecretCreateRequest(scope=SecretScope.EXCHANGE, name="api_key", value="super-secret"))
    assert public.name == "api_key"
    secrets = await service.list_secrets()
    assert "super-secret" not in str(secrets)
    resolved = await service.resolve_secret("default", "api_key")
    assert resolved == "super-secret"
