import pytest
from app.mobile_v1.application.service import MobileServiceV1
from app.mobile_v1.domain.models import MobileDevice, MobilePlatform, MobilePushMessage

@pytest.mark.asyncio
async def test_mobile_push_dryrun():
    service = MobileServiceV1()
    await service.register_device(MobileDevice(device_id="d1", platform=MobilePlatform.ANDROID, push_token="token"))
    result = await service.send_push("d1", MobilePushMessage(title="Hi", body="Test"))
    assert result.accepted is True
    assert result.provider_message_id.startswith("push_dryrun_")
