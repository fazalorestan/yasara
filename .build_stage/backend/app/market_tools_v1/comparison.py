from pydantic import BaseModel
from app.multi_exchange_v1.domain.models import SupportedExchange

class ExchangePriceItemV1(BaseModel):
    exchange: SupportedExchange
    symbol: str
    price: float

class ExchangeComparisonResultV1(BaseModel):
    symbol: str
    best_bid_exchange: SupportedExchange | None = None
    lowest_price_exchange: SupportedExchange | None = None
    price_range: float = 0

class ExchangeComparisonEngineV1:
    def compare_prices(self, items: list[ExchangePriceItemV1]) -> ExchangeComparisonResultV1:
        if not items:
            return ExchangeComparisonResultV1(symbol="")
        sorted_items = sorted(items, key=lambda x: x.price)
        return ExchangeComparisonResultV1(
            symbol=items[0].symbol,
            lowest_price_exchange=sorted_items[0].exchange,
            best_bid_exchange=sorted_items[-1].exchange,
            price_range=sorted_items[-1].price - sorted_items[0].price,
        )
