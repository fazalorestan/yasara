from app.mobile_v1.domain.models import MobileDevice, MobileOfflineSyncPayload, MobilePushMessage, MobileSettings
from app.mobile_v1.engine.home_builder import MobileHomeBuilderV1
from app.mobile_v1.engine.push import MobilePushEngineV1
from app.mobile_v1.repository.memory import InMemoryMobileRepositoryV1

class MobileServiceV1:
    def __init__(self):
        self.repository = InMemoryMobileRepositoryV1()
        self.home_builder = MobileHomeBuilderV1()
        self.push_engine = MobilePushEngineV1()

    async def register_device(self, device: MobileDevice):
        return self.repository.register_device(device)

    async def list_devices(self, owner_id: str = "default"):
        return self.repository.list_devices(owner_id)

    async def disable_device(self, device_id: str):
        return self.repository.disable_device(device_id)

    async def get_settings(self, owner_id: str = "default"):
        return self.repository.get_settings(owner_id)

    async def save_settings(self, settings: MobileSettings):
        return self.repository.save_settings(settings)

    async def home(self, owner_id: str = "default"):
        return await self.home_builder.build(owner_id)

    async def offline_sync(self, owner_id: str = "default"):
        settings = self.repository.get_settings(owner_id)
        home = await self.home_builder.build(owner_id)
        return MobileOfflineSyncPayload(owner_id=owner_id, settings=settings, home=home)

    async def send_push(self, device_id: str, message: MobilePushMessage):
        device = self.repository.devices.get(device_id)
        if device is None:
            return None
        return await self.push_engine.send(device, message)

mobile_service_v1 = MobileServiceV1()
