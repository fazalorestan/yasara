import asyncio
import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
import websockets
from app.market_data.domain.events import MarketEventType
from app.market_data.infrastructure.binance_normalizer import BinanceStreamNormalizer
from app.market_data.infrastructure.event_bus import market_event_bus

@dataclass
class StreamSubscription:
    symbol: str
    stream_type: str
    timeframe: str | None = None

    @property
    def stream_name(self) -> str:
        symbol = self.symbol.replace("/", "").lower()
        if self.stream_type == "kline":
            return f"{symbol}@kline_{self.timeframe or '1m'}"
        if self.stream_type == "ticker":
            return f"{symbol}@ticker"
        if self.stream_type == "depth":
            return f"{symbol}@depth20@100ms"
        return f"{symbol}@ticker"

@dataclass
class WebSocketStats:
    connected: bool = False
    reconnect_count: int = 0
    messages_received: int = 0
    messages_published: int = 0
    last_message_at: datetime | None = None
    last_error: str = ""

class BinanceWebSocketManager:
    def __init__(self, base_url: str = "wss://fstream.binance.com/stream"):
        self.base_url = base_url
        self.normalizer = BinanceStreamNormalizer()
        self.subscriptions: dict[str, StreamSubscription] = {}
        self.stats = WebSocketStats()
        self._task: asyncio.Task | None = None
        self._running = False

    def subscribe_kline(self, symbol: str, timeframe: str = "1m") -> None:
        sub = StreamSubscription(symbol=symbol, stream_type="kline", timeframe=timeframe)
        self.subscriptions[sub.stream_name] = sub

    def subscribe_ticker(self, symbol: str) -> None:
        sub = StreamSubscription(symbol=symbol, stream_type="ticker")
        self.subscriptions[sub.stream_name] = sub

    def subscribe_depth(self, symbol: str) -> None:
        sub = StreamSubscription(symbol=symbol, stream_type="depth")
        self.subscriptions[sub.stream_name] = sub

    async def start(self) -> None:
        if self._running:
            return
        await market_event_bus.start()
        self._running = True
        self._task = asyncio.create_task(self._run(), name="binance-ws-manager")

    async def stop(self) -> None:
        self._running = False
        if self._task:
            self._task.cancel()
            try:
                await self._task
            except asyncio.CancelledError:
                pass
            self._task = None
        self.stats.connected = False

    async def _run(self) -> None:
        backoff = 1.0
        while self._running:
            if not self.subscriptions:
                await asyncio.sleep(0.5)
                continue
            streams = "/".join(sorted(self.subscriptions))
            url = f"{self.base_url}?streams={streams}"
            try:
                async with websockets.connect(url, ping_interval=20, ping_timeout=20) as ws:
                    self.stats.connected = True
                    self.stats.last_error = ""
                    backoff = 1.0
                    async for message in ws:
                        await self._handle_message(message)
            except asyncio.CancelledError:
                raise
            except Exception as exc:
                self.stats.connected = False
                self.stats.reconnect_count += 1
                self.stats.last_error = str(exc)
                await asyncio.sleep(backoff)
                backoff = min(backoff * 2, 30)

    async def _handle_message(self, message: str) -> None:
        self.stats.messages_received += 1
        self.stats.last_message_at = datetime.now(timezone.utc)
        raw = json.loads(message)
        data = raw.get("data", raw)
        event = None
        if data.get("e") == "kline":
            event = self.normalizer.kline_event(data)
        elif data.get("e") == "24hrTicker":
            event = self.normalizer.ticker_event(data)
        elif "b" in data and "a" in data:
            event = self.normalizer.depth_event(data)
        if event:
            await market_event_bus.publish(event)
            self.stats.messages_published += 1

binance_ws_manager = BinanceWebSocketManager()
