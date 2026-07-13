from dataclasses import dataclass, field
from typing import Any, Callable
from app.platform_core.clock import utc_now_iso

@dataclass
class PlatformEvent:
    name: str
    payload: dict[str, Any] = field(default_factory=dict)
    source: str = "system"
    ts: str = field(default_factory=utc_now_iso)

class EventBus:
    def __init__(self):
        self._handlers: dict[str, list[Callable[[PlatformEvent], None]]] = {}
        self._history: list[PlatformEvent] = []

    def subscribe(self, event_name: str, handler: Callable[[PlatformEvent], None]):
        self._handlers.setdefault(event_name, []).append(handler)

    def publish(self, event: PlatformEvent):
        self._history.append(event)
        for handler in self._handlers.get(event.name, []):
            handler(event)
        for handler in self._handlers.get("*", []):
            handler(event)
        return event

    def history(self, limit: int = 100):
        return self._history[-limit:]

event_bus = EventBus()
