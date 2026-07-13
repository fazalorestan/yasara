from app.platform_core.release_candidate.release_health import InternalRCReleaseHealth

def test_health(): assert InternalRCReleaseHealth().health()['system_auto_reenable_blocked'] is True
