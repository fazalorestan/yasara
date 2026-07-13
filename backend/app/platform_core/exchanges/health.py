from app.platform_core.exchanges.models import ExchangeHealth

class ExchangeHealthMonitor:
    def __init__(self):
        self._items = {}

    def seed_defaults(self, exchange_ids: list[str]):
        for exchange_id in exchange_ids:
            if exchange_id not in self._items:
                self._items[exchange_id] = ExchangeHealth(exchange_id=exchange_id)
        return self.snapshot()

    def set_status(self, exchange_id: str, status: str):
        self._items[exchange_id] = ExchangeHealth(exchange_id=exchange_id, status=status)
        return self._items[exchange_id].__dict__

    def snapshot(self):
        return {k: v.__dict__ for k, v in self._items.items()}

exchange_health_monitor = ExchangeHealthMonitor()
