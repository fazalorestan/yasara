import pytest
from app.account_sync_v1.application.service import AccountSyncServiceV1

@pytest.mark.asyncio
async def test_account_sync_snapshot_success():
    service = AccountSyncServiceV1()
    snapshot = await service.sync_account("default")
    assert snapshot.status == "success"
    assert "USDT" in snapshot.balances
