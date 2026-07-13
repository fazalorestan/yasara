from app.platform_core.clock import platform_clock, utc_now_iso

def test_v429_clock():
    now = platform_clock.now_utc()
    assert now.tzinfo is not None
    assert "+00:00" in utc_now_iso()
