from app.platform_core.exchanges.models import ExchangeCapability

class ExchangeCapabilityMatrix:
    def __init__(self):
        self._items = {}

    def seed_defaults(self):
        if not self._items:
            futures_exchanges = {"binance", "bybit", "okx", "kucoin", "gate", "mexc", "bitget", "bingx", "bitunix", "toobit", "lbank"}
            sandbox_exchanges = {"binance", "bybit", "okx", "bitunix", "toobit"}
            iran_exchanges = {"nobitex", "wallex", "tabdeal", "ramzinex", "exir", "bitpin", "ompfinex"}
            for exchange_id in futures_exchanges | iran_exchanges:
                self._items[exchange_id] = ExchangeCapability(
                    spot=True,
                    futures=exchange_id in futures_exchanges,
                    rest=True,
                    websocket=exchange_id in futures_exchanges,
                    sandbox=exchange_id in sandbox_exchanges,
                    testnet=exchange_id in sandbox_exchanges,
                    iran_market=exchange_id in iran_exchanges,
                )
        return {k: v.__dict__ for k, v in self._items.items()}

    def get(self, exchange_id: str):
        self.seed_defaults()
        item = self._items.get(exchange_id.lower())
        return item.__dict__ if item else None

exchange_capability_matrix = ExchangeCapabilityMatrix()
