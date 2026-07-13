from app.mobile_v1.domain.models import MobileDevice, MobilePlatform
from app.mobile_v1.repository.memory import InMemoryMobileRepositoryV1

def test_mobile_device_register_and_disable():
    repo = InMemoryMobileRepositoryV1()
    device = repo.register_device(MobileDevice(device_id="d1", platform=MobilePlatform.ANDROID, push_token="token"))
    assert device.device_id == "d1"
    assert len(repo.list_devices()) == 1
    repo.disable_device("d1")
    assert len(repo.list_devices()) == 0
