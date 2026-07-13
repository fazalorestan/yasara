import asyncio
from collections import defaultdict
from collections.abc import Awaitable, Callable
from app.market_data.domain.events import MarketEvent, MarketEventType

EventHandler = Callable[[MarketEvent], Awaitable[None]]

class AsyncMarketEventBus:
    def __init__(self):
        self._subscribers: dict[str, list[EventHandler]] = defaultdict(list)
        self._queue: asyncio.Queue[MarketEvent] = asyncio.Queue()
        self._task: asyncio.Task | None = None
        self._running = False
        self.published = 0
        self.delivered = 0

    def subscribe(self, event_type: MarketEventType | str, handler: EventHandler) -> None:
        self._subscribers[str(event_type)].append(handler)

    async def publish(self, event: MarketEvent) -> None:
        self.published += 1
        await self._queue.put(event)

    async def start(self) -> None:
        if self._running:
            return
        self._running = True
        self._task = asyncio.create_task(self._run(), name="yasara-market-event-bus")

    async def stop(self) -> None:
        self._running = False
        if self._task:
            self._task.cancel()
            try:
                await self._task
            except asyncio.CancelledError:
                pass
            self._task = None

    async def _run(self) -> None:
        while self._running:
            event = await self._queue.get()
            handlers = list(self._subscribers.get(str(event.event_type), [])) + list(self._subscribers.get("*", []))
            for handler in handlers:
                await handler(event)
                self.delivered += 1

    def stats(self) -> dict:
        return {
            "running": self._running,
            "published": self.published,
            "delivered": self.delivered,
            "queue_size": self._queue.qsize(),
            "subscriber_groups": len(self._subscribers),
        }

market_event_bus = AsyncMarketEventBus()
