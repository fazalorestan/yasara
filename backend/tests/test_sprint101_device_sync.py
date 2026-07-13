from app.cloud_v1.device_sync import DeviceStateV1, DeviceSyncServiceV1

def test_device_sync_needs_sync():
    assert DeviceSyncServiceV1().needs_sync(DeviceStateV1(device_id="d", last_version=1), DeviceStateV1(device_id="d", last_version=2)) is True
