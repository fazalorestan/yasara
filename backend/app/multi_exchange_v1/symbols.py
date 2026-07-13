from app.multi_exchange_v1.domain.models import SupportedExchange

class SymbolMapperV1:
    def normalize(self, symbol: str) -> str:
        return symbol.upper().replace("-", "/").replace("_", "/")

    def to_exchange_symbol(self, exchange: SupportedExchange, symbol: str) -> str:
        return self.normalize(symbol).replace("/", "")

    def from_exchange_symbol(self, exchange: SupportedExchange, symbol: str) -> str:
        symbol = symbol.upper().replace("-", "").replace("_", "")
        if symbol.endswith("USDT") and "/" not in symbol:
            return symbol[:-4] + "/USDT"
        return symbol
