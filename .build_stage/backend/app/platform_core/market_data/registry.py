from app.platform_core.market_data.models import MarketSymbol

class MarketDataRegistry:
    def __init__(self):
        self._symbols: dict[str, MarketSymbol] = {}

    def register_symbol(self, symbol: MarketSymbol):
        self._symbols[symbol.symbol] = symbol
        return symbol

    def seed_defaults(self):
        if not self._symbols:
            self.register_symbol(MarketSymbol(symbol="BTCUSDT", base_asset="BTC", quote_asset="USDT", exchange="internal"))
            self.register_symbol(MarketSymbol(symbol="ETHUSDT", base_asset="ETH", quote_asset="USDT", exchange="internal"))
            self.register_symbol(MarketSymbol(symbol="XAUUSD", base_asset="XAU", quote_asset="USD", market_type="forex", exchange="internal"))
            self.register_symbol(MarketSymbol(symbol="IRAN_INDEX", base_asset="IRAN", quote_asset="INDEX", market_type="iran_market", exchange="internal"))
        return self.list_symbols()

    def get_symbol(self, symbol: str):
        self.seed_defaults()
        item = self._symbols.get(symbol)
        return item.__dict__ if item else None

    def list_symbols(self):
        return {k: v.__dict__ for k, v in self._symbols.items()}

market_data_registry = MarketDataRegistry()
