from app.v11_market_data.models import MarketTickerV11
from app.v11_market_data.symbol_registry import SymbolRegistryV11


class RestFallbackProviderV11:
    def __init__(self):
        self.registry = SymbolRegistryV11()

    def synthetic_ticker(self, exchange: str, symbol: str, last_price: float = 100.0) -> MarketTickerV11:
        normalized = self.registry.normalize(symbol)
        return MarketTickerV11(
            exchange=exchange.lower(),
            symbol=symbol,
            normalized_symbol=normalized,
            last_price=last_price,
            bid=last_price - 0.5,
            ask=last_price + 0.5,
            volume_24h=0.0,
        )
