from app.v432_platform_versioning.service import PlatformVersioningServiceV432

def test_v432_service():
    s = PlatformVersioningServiceV432()
    assert s.summary().ready is True
    assert s.upgrade_path()["ready"] is True
