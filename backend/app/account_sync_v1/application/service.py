from app.account_sync_v1.engine.listen_key import ListenKeyManagerV1
from app.account_sync_v1.engine.order_recovery import OrderRecoveryEngineV1
from app.account_sync_v1.engine.stream_manager import UserDataStreamManagerV1
from app.account_sync_v1.engine.synchronizer import AccountSynchronizerV1

class AccountSyncServiceV1:
    def __init__(self):
        self.listen_keys = ListenKeyManagerV1()
        self.stream = UserDataStreamManagerV1(self.listen_keys)
        self.synchronizer = AccountSynchronizerV1()
        self.recovery = OrderRecoveryEngineV1()

    async def create_listen_key(self, owner_id: str = "default"):
        return await self.listen_keys.create(owner_id)

    async def keepalive(self, owner_id: str = "default"):
        return await self.listen_keys.keepalive(owner_id)

    async def connect_stream(self, owner_id: str = "default"):
        return await self.stream.connect(owner_id)

    async def disconnect_stream(self):
        return await self.stream.disconnect()

    async def ingest_event(self, owner_id: str, payload: dict):
        return await self.stream.ingest(owner_id, payload)

    async def stream_history(self):
        return self.stream.history()

    async def sync_account(self, owner_id: str = "default"):
        return await self.synchronizer.sync(owner_id)

    async def recover_orders(self, owner_id: str = "default", local_orders: list[dict] | None = None):
        snapshot = await self.synchronizer.sync(owner_id)
        return self.recovery.recover(snapshot, local_orders)

account_sync_service_v1 = AccountSyncServiceV1()
