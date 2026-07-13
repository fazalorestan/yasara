from pydantic import BaseModel, Field

class ScreenerInputItemV1(BaseModel):
    symbol: str
    price: float
    change_percent: float = 0
    volume: float = 0

class ScreenerFilterV1(BaseModel):
    min_change_percent: float | None = None
    min_volume: float | None = None
    max_price: float | None = None

class MarketScreenerV1:
    def filter(self, items: list[ScreenerInputItemV1], criteria: ScreenerFilterV1) -> list[ScreenerInputItemV1]:
        result = []
        for item in items:
            if criteria.min_change_percent is not None and item.change_percent < criteria.min_change_percent:
                continue
            if criteria.min_volume is not None and item.volume < criteria.min_volume:
                continue
            if criteria.max_price is not None and item.price > criteria.max_price:
                continue
            result.append(item)
        return result
