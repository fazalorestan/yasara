from datetime import datetime, timezone
from app.secrets_v1.domain.models import SecretRecord, SecretStatus

class InMemorySecretRepositoryV1:
    def __init__(self):
        self._records: dict[str, SecretRecord] = {}

    def save(self, record: SecretRecord) -> SecretRecord:
        record.updated_at = datetime.now(timezone.utc)
        self._records[record.secret_id] = record
        return record

    def find_by_owner_name(self, owner_id: str, name: str) -> SecretRecord | None:
        for record in self._records.values():
            if record.owner_id == owner_id and record.name == name and record.status == SecretStatus.ACTIVE:
                return record
        return None

    def list_by_owner(self, owner_id: str) -> list[SecretRecord]:
        return [r for r in self._records.values() if r.owner_id == owner_id]

    def disable(self, secret_id: str) -> SecretRecord | None:
        record = self._records.get(secret_id)
        if record:
            record.status = SecretStatus.DISABLED
            record.updated_at = datetime.now(timezone.utc)
        return record
