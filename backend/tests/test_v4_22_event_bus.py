from app.platform_core.kernel.event_bus import EventBus, PlatformEvent

def test_v422_event_bus():
    b=EventBus(); got=[]; b.subscribe('SignalGenerated', lambda e: got.append(e.name)); b.publish(PlatformEvent(name='SignalGenerated')); assert got==['SignalGenerated']
