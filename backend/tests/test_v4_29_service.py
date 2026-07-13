from app.v429_timezone_runtime.service import TimezoneRuntimeServiceV429

def test_v429_service():
    s = TimezoneRuntimeServiceV429()
    assert s.summary().ready is True
    assert s.now()["timezone_safe"] is True
    assert s.smoke()["ready"] is True
