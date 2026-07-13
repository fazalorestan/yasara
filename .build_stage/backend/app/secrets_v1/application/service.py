import uuid
from app.secrets_v1.domain.models import SecretCreateRequest, SecretPublicView, SecretRecord
from app.secrets_v1.engine.crypto import SecretCryptoEngineV1
from app.secrets_v1.repository.memory import InMemorySecretRepositoryV1

class SecretsVaultServiceV1:
    def __init__(self):
        self.crypto = SecretCryptoEngineV1()
        self.repository = InMemorySecretRepositoryV1()

    async def create_secret(self, payload: SecretCreateRequest) -> SecretPublicView:
        record = SecretRecord(
            secret_id=uuid.uuid4().hex,
            owner_id=payload.owner_id,
            scope=payload.scope,
            name=payload.name,
            encrypted_value=self.crypto.encrypt(payload.value),
            metadata=payload.metadata,
        )
        self.repository.save(record)
        return self._public(record)

    async def resolve_secret(self, owner_id: str, name: str) -> str | None:
        record = self.repository.find_by_owner_name(owner_id, name)
        return self.crypto.decrypt(record.encrypted_value) if record else None

    async def list_secrets(self, owner_id: str = "default") -> list[SecretPublicView]:
        return [self._public(r) for r in self.repository.list_by_owner(owner_id)]

    async def disable_secret(self, secret_id: str) -> SecretPublicView | None:
        record = self.repository.disable(secret_id)
        return self._public(record) if record else None

    def _public(self, record: SecretRecord) -> SecretPublicView:
        return SecretPublicView(
            secret_id=record.secret_id,
            owner_id=record.owner_id,
            scope=record.scope,
            name=record.name,
            status=record.status,
            metadata=record.metadata,
            created_at=record.created_at,
            updated_at=record.updated_at,
        )

secrets_vault_service_v1 = SecretsVaultServiceV1()
