from app.platform_core.kernel.event_bus import PlatformEvent

def test_v429_event_bus_timezone():
    e = PlatformEvent(name="x")
    assert "+00:00" in e.ts
