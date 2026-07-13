from pydantic import BaseModel, Field


class SymbolMappingV11(BaseModel):
    raw: str
    normalized: str


class SymbolRegistryV11:
    def normalize(self, symbol: str) -> str:
        cleaned = symbol.upper().replace("-", "").replace("_", "").replace("/", "")
        if cleaned.endswith("USDT"):
            return cleaned
        return cleaned

    def exchange_symbol(self, exchange: str, symbol: str) -> str:
        normalized = self.normalize(symbol)
        if exchange.lower() in {"bitunix", "toobit"}:
            if normalized.endswith("USDT"):
                base = normalized[:-4]
                return f"{base}-USDT"
        return normalized

    def mapping(self, symbol: str) -> SymbolMappingV11:
        return SymbolMappingV11(raw=symbol, normalized=self.normalize(symbol))


class SymbolRegistrySummaryV11(BaseModel):
    examples: list[SymbolMappingV11] = Field(default_factory=list)


class SymbolRegistrySummaryBuilderV11:
    def build(self) -> SymbolRegistrySummaryV11:
        registry = SymbolRegistryV11()
        return SymbolRegistrySummaryV11(examples=[
            registry.mapping("BTCUSDT"),
            registry.mapping("BTC-USDT"),
            registry.mapping("BTC_USDT"),
            registry.mapping("BTC/USDT"),
        ])
