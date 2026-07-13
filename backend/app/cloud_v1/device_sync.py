from pydantic import BaseModel, Field

class DeviceStateV1(BaseModel):
    device_id: str
    last_version: int = 0
    data: dict = Field(default_factory=dict)

class DeviceSyncServiceV1:
    def needs_sync(self, local: DeviceStateV1, remote: DeviceStateV1) -> bool:
        return local.last_version != remote.last_version
