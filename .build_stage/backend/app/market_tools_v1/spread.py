from pydantic import BaseModel

class SpreadInputV1(BaseModel):
    symbol: str
    bid: float
    ask: float

class SpreadResultV1(BaseModel):
    symbol: str
    spread: float
    spread_percent: float

class SpreadMonitorV1:
    def calculate(self, item: SpreadInputV1) -> SpreadResultV1:
        spread = max(0.0, item.ask - item.bid)
        mid = (item.ask + item.bid) / 2 if (item.ask + item.bid) else 0
        spread_percent = (spread / mid * 100) if mid else 0
        return SpreadResultV1(symbol=item.symbol, spread=spread, spread_percent=spread_percent)
