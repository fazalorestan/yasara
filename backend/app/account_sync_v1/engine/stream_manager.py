from datetime import datetime, timezone
from app.account_sync_v1.domain.models import AccountStreamEvent, StreamConnectionStatus, StreamState
from app.account_sync_v1.engine.listen_key import ListenKeyManagerV1
from app.account_sync_v1.engine.normalizer import BinanceUserDataEventNormalizerV1

class UserDataStreamManagerV1:
    def __init__(self, listen_keys: ListenKeyManagerV1):
        self.listen_keys = listen_keys
        self.normalizer = BinanceUserDataEventNormalizerV1()
        self.state = StreamState()
        self.events: list[AccountStreamEvent] = []

    async def connect(self, owner_id: str = "default") -> StreamState:
        record = await self.listen_keys.keepalive(owner_id)
        self.state = StreamState(
            owner_id=owner_id,
            status=StreamConnectionStatus.CONNECTED,
            listen_key=record.listen_key,
            updated_at=datetime.now(timezone.utc),
        )
        return self.state

    async def disconnect(self) -> StreamState:
        self.state.status = StreamConnectionStatus.DISCONNECTED
        self.state.updated_at = datetime.now(timezone.utc)
        return self.state

    async def ingest(self, owner_id: str, payload: dict) -> AccountStreamEvent:
        event = self.normalizer.normalize(owner_id, payload)
        self.events.append(event)
        self.state.events_received += 1
        self.state.updated_at = datetime.now(timezone.utc)
        return event

    async def reconnect(self) -> StreamState:
        self.state.status = StreamConnectionStatus.RECONNECTING
        self.state.reconnect_count += 1
        self.state.updated_at = datetime.now(timezone.utc)
        return await self.connect(self.state.owner_id)

    def history(self) -> list[AccountStreamEvent]:
        return list(self.events)
