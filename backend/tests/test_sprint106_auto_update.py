from app.cloud_v1.auto_update import AutoUpdateCheckV1, AutoUpdateServiceV1

def test_auto_update_available():
    result = AutoUpdateServiceV1().check(AutoUpdateCheckV1(current_version="1.0.0", latest_version="1.1.0"))
    assert result.update_available is True
