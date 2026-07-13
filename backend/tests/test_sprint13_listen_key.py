import pytest
from app.account_sync_v1.engine.listen_key import ListenKeyManagerV1

@pytest.mark.asyncio
async def test_listen_key_create_and_keepalive():
    manager = ListenKeyManagerV1()
    first = await manager.create("u1")
    second = await manager.keepalive("u1")
    assert second.listen_key == first.listen_key
    assert second.keepalive_count == 1
