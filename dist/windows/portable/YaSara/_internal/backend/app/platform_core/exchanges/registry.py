from app.platform_core.exchanges.models import ExchangeInfo

class ExchangeRegistry:
    def __init__(self):
        self._items = {}

    def register(self, exchange: ExchangeInfo):
        self._items[exchange.exchange_id] = exchange
        return exchange

    def seed_defaults(self):
        if not self._items:
            global_exchanges = [
                ("binance", "Binance"), ("bybit", "Bybit"), ("okx", "OKX"), ("kucoin", "KuCoin"),
                ("gate", "Gate"), ("mexc", "MEXC"), ("bitget", "Bitget"), ("bingx", "BingX"),
                ("bitunix", "Bitunix"), ("toobit", "Toobit"), ("lbank", "LBank")
            ]
            iran_exchanges = [
                ("nobitex", "Nobitex"), ("wallex", "Wallex"), ("tabdeal", "Tabdeal"),
                ("ramzinex", "Ramzinex"), ("exir", "Exir"), ("bitpin", "Bitpin"), ("ompfinex", "OMPFinex")
            ]
            for exchange_id, name in global_exchanges:
                self.register(ExchangeInfo(exchange_id=exchange_id, name=name, exchange_type="crypto", region="global"))
            for exchange_id, name in iran_exchanges:
                self.register(ExchangeInfo(exchange_id=exchange_id, name=name, exchange_type="crypto", region="iran"))
        return self.list()

    def list(self):
        return {k: v.__dict__ for k, v in self._items.items()}

    def get(self, exchange_id: str):
        self.seed_defaults()
        item = self._items.get(exchange_id.lower())
        return item.__dict__ if item else None

exchange_registry = ExchangeRegistry()
