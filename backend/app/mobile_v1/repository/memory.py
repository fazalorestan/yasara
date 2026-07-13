from datetime import datetime, timezone
from app.mobile_v1.domain.models import MobileDevice, MobileSettings

class InMemoryMobileRepositoryV1:
    def __init__(self):
        self.devices: dict[str, MobileDevice] = {}
        self.settings: dict[str, MobileSettings] = {}

    def register_device(self, device: MobileDevice) -> MobileDevice:
        device.last_seen_at = datetime.now(timezone.utc)
        self.devices[device.device_id] = device
        return device

    def list_devices(self, owner_id: str = "default") -> list[MobileDevice]:
        return [d for d in self.devices.values() if d.owner_id == owner_id and d.enabled]

    def disable_device(self, device_id: str) -> MobileDevice | None:
        device = self.devices.get(device_id)
        if device:
            device.enabled = False
            device.last_seen_at = datetime.now(timezone.utc)
        return device

    def get_settings(self, owner_id: str = "default") -> MobileSettings:
        if owner_id not in self.settings:
            self.settings[owner_id] = MobileSettings(owner_id=owner_id)
        return self.settings[owner_id]

    def save_settings(self, settings: MobileSettings) -> MobileSettings:
        settings.updated_at = datetime.now(timezone.utc)
        self.settings[settings.owner_id] = settings
        return settings
