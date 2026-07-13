from pydantic import BaseModel, Field
from app.multi_exchange_v1.domain.models import SupportedExchange
from app.multi_exchange_v1.symbols import SymbolMapperV1

class ExchangeSymbolInfoV1(BaseModel):
    exchange: SupportedExchange
    unified_symbol: str
    exchange_symbol: str
    base_asset: str
    quote_asset: str
    enabled: bool = True
    metadata: dict = Field(default_factory=dict)

class SymbolRegistryV1:
    def __init__(self):
        self.mapper = SymbolMapperV1()
        self._items: dict[str, ExchangeSymbolInfoV1] = {}
        self.register_defaults()

    def key(self, exchange: SupportedExchange, unified_symbol: str) -> str:
        return f"{exchange}:{unified_symbol.upper()}"

    def register(self, exchange: SupportedExchange, unified_symbol: str, metadata: dict | None = None) -> ExchangeSymbolInfoV1:
        normalized = self.mapper.normalize(unified_symbol)
        if "/" in normalized:
            base, quote = normalized.split("/", 1)
        else:
            base, quote = normalized[:-4], normalized[-4:]
        item = ExchangeSymbolInfoV1(
            exchange=exchange,
            unified_symbol=normalized,
            exchange_symbol=self.mapper.to_exchange_symbol(exchange, normalized),
            base_asset=base,
            quote_asset=quote,
            metadata=metadata or {},
        )
        self._items[self.key(exchange, normalized)] = item
        return item

    def get(self, exchange: SupportedExchange, unified_symbol: str) -> ExchangeSymbolInfoV1 | None:
        return self._items.get(self.key(exchange, self.mapper.normalize(unified_symbol)))

    def list(self, exchange: SupportedExchange | None = None) -> list[ExchangeSymbolInfoV1]:
        items = list(self._items.values())
        return [i for i in items if i.exchange == exchange] if exchange else items

    def register_defaults(self):
        for exchange in [SupportedExchange.BITUNIX, SupportedExchange.TOOBIT]:
            for symbol in ["BTC/USDT", "ETH/USDT", "BNB/USDT"]:
                self.register(exchange, symbol)

symbol_registry_v1 = SymbolRegistryV1()
