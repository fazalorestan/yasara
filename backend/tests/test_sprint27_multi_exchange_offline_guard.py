import pytest
from app.multi_exchange_v1.clients.offline_guard import OfflineNetworkGuardClientV1

@pytest.mark.asyncio
async def test_offline_guard_blocks_network_access():
    with pytest.raises(RuntimeError) as exc:
        await OfflineNetworkGuardClientV1().get_json("https://example.com", {"symbol": "BTCUSDT"})
    assert "Network access is disabled" in str(exc.value)
