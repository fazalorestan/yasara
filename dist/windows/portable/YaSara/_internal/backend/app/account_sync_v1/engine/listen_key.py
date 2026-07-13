import uuid
from datetime import datetime, timezone, timedelta
from app.account_sync_v1.domain.models import ListenKeyRecord
from app.exchange_private_v1.domain.models import PrivateExchange

class ListenKeyManagerV1:
    def __init__(self):
        self._records: dict[str, ListenKeyRecord] = {}

    async def create(self, owner_id: str = "default", exchange: PrivateExchange = PrivateExchange.BINANCE_FUTURES) -> ListenKeyRecord:
        record = ListenKeyRecord(
            owner_id=owner_id,
            exchange=exchange,
            listen_key=f"dryrun_listen_{uuid.uuid4().hex}",
            dry_run=True,
        )
        self._records[self._key(owner_id, exchange)] = record
        return record

    async def get(self, owner_id: str = "default", exchange: PrivateExchange = PrivateExchange.BINANCE_FUTURES) -> ListenKeyRecord | None:
        return self._records.get(self._key(owner_id, exchange))

    async def keepalive(self, owner_id: str = "default", exchange: PrivateExchange = PrivateExchange.BINANCE_FUTURES) -> ListenKeyRecord:
        record = await self.get(owner_id, exchange)
        if record is None or record.expired:
            record = await self.create(owner_id, exchange)
        else:
            record.keepalive_count += 1
            record.expires_at = datetime.now(timezone.utc) + timedelta(minutes=55)
        return record

    def _key(self, owner_id: str, exchange: PrivateExchange) -> str:
        return f"{exchange}:{owner_id}"
