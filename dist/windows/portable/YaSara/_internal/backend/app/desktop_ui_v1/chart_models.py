from datetime import datetime, timezone
from pydantic import BaseModel, Field

class ChartCandleV1(BaseModel):
    time: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    open: float
    high: float
    low: float
    close: float
    volume: float = 0

class ChartSeriesV1(BaseModel):
    symbol: str
    timeframe: str
    candles: list[ChartCandleV1] = Field(default_factory=list)

class ChartSeriesBuilderV1:
    def from_ohlcv_rows(self, symbol: str, timeframe: str, rows: list[dict]) -> ChartSeriesV1:
        candles = [ChartCandleV1(
            open=float(r.get("open", 0)),
            high=float(r.get("high", 0)),
            low=float(r.get("low", 0)),
            close=float(r.get("close", 0)),
            volume=float(r.get("volume", 0)),
        ) for r in rows]
        return ChartSeriesV1(symbol=symbol, timeframe=timeframe, candles=candles)
