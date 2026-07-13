from time import time
from app.v11_market_data.models import ConnectionStateV11, ExchangeHealthV11


class MarketHealthMonitorV11:
    def __init__(self):
        self._health: dict[str, ExchangeHealthV11] = {}

    def set_state(self, exchange: str, state: ConnectionStateV11, message: str = "") -> ExchangeHealthV11:
        item = self._health.get(exchange.lower()) or ExchangeHealthV11(
            exchange=exchange.lower(),
            state=state,
        )
        item.state = state
        item.message = message
        if state == ConnectionStateV11.CONNECTED:
            item.last_heartbeat = time()
        self._health[exchange.lower()] = item
        return item

    def heartbeat(self, exchange: str) -> ExchangeHealthV11:
        return self.set_state(exchange, ConnectionStateV11.CONNECTED, "heartbeat")

    def reconnecting(self, exchange: str) -> ExchangeHealthV11:
        item = self._health.get(exchange.lower()) or ExchangeHealthV11(
            exchange=exchange.lower(),
            state=ConnectionStateV11.RECONNECTING,
        )
        item.state = ConnectionStateV11.RECONNECTING
        item.reconnect_attempts += 1
        item.message = "reconnecting"
        self._health[exchange.lower()] = item
        return item

    def all(self) -> list[ExchangeHealthV11]:
        return list(self._health.values())

    def is_ready(self) -> bool:
        return all(h.state == ConnectionStateV11.CONNECTED for h in self._health.values()) if self._health else True
