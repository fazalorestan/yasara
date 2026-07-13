from app.v11_market_data.health import MarketHealthMonitorV11
from app.v11_market_data.models import ConnectionStateV11


class WebSocketManagerV11:
    def __init__(self, health: MarketHealthMonitorV11 | None = None):
        self.health = health or MarketHealthMonitorV11()
        self.connections: set[str] = set()

    def connect(self, exchange: str) -> None:
        key = exchange.lower()
        self.connections.add(key)
        self.health.set_state(key, ConnectionStateV11.CONNECTED, "connected")

    def disconnect(self, exchange: str) -> None:
        key = exchange.lower()
        self.connections.discard(key)
        self.health.set_state(key, ConnectionStateV11.DISCONNECTED, "disconnected")

    def reconnect(self, exchange: str) -> None:
        key = exchange.lower()
        self.health.reconnecting(key)
        self.connect(key)

    def is_connected(self, exchange: str) -> bool:
        return exchange.lower() in self.connections
