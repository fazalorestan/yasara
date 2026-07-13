from datetime import datetime, timezone
from app.account_sync_v1.domain.models import AccountSyncSnapshot, SyncStatus
from app.exchange_private_v1.application.service import private_exchange_service_v1

class AccountSynchronizerV1:
    async def sync(self, owner_id: str = "default") -> AccountSyncSnapshot:
        snapshot = AccountSyncSnapshot(owner_id=owner_id, status=SyncStatus.RUNNING)
        try:
            balances = await private_exchange_service_v1.balances(owner_id)
            positions = await private_exchange_service_v1.positions(owner_id)
            snapshot.balances = balances.balances
            snapshot.positions = positions.positions
            snapshot.open_orders = []
            snapshot.status = SyncStatus.SUCCESS
            snapshot.synced_at = datetime.now(timezone.utc)
            return snapshot
        except Exception as exc:
            snapshot.status = SyncStatus.FAILED
            snapshot.last_error = str(exc)
            snapshot.synced_at = datetime.now(timezone.utc)
            return snapshot
