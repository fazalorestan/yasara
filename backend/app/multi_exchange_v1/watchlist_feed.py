from pydantic import BaseModel, Field
from app.multi_exchange_v1.domain.models import SupportedExchange
from app.multi_exchange_v1.router_engine import ExchangeRouterEngineV1

class MultiExchangeWatchlistRequestV1(BaseModel):
    symbols: list[str] = Field(default_factory=lambda: ["BTC/USDT", "ETH/USDT"])
    preferred_exchange: SupportedExchange | None = None

class MultiExchangeWatchlistItemV1(BaseModel):
    symbol: str
    selected_exchange: SupportedExchange
    price: float = 0
    status: str = "ok"

class MultiExchangeWatchlistFeedV1:
    def __init__(self):
        self.router = ExchangeRouterEngineV1()

    async def build(self, request: MultiExchangeWatchlistRequestV1, service) -> list[MultiExchangeWatchlistItemV1]:
        items = []
        for symbol in request.symbols:
            decision = self.router.choose(symbol, request.preferred_exchange)
            ticker = await service.ticker(decision.selected_exchange, symbol)
            price = ticker.price if hasattr(ticker, "price") else float((ticker or {}).get("price", 0))
            items.append(MultiExchangeWatchlistItemV1(symbol=symbol, selected_exchange=decision.selected_exchange, price=price))
        return items
