import pytest
from app.mobile_v1.application.service import MobileServiceV1

@pytest.mark.asyncio
async def test_mobile_home_payload_builds():
    payload = await MobileServiceV1().home("default")
    assert payload.owner_id == "default"
    assert payload.portfolio.equity >= 0
    assert len(payload.watchlist) >= 1
