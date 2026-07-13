from datetime import datetime, timezone
from pydantic import BaseModel, Field
from app.multi_exchange_v1.domain.models import SupportedExchange

class MarketTickerSnapshotItemV1(BaseModel):
    exchange: SupportedExchange
    symbol: str
    price: float
    change_percent: float = 0
    volume: float = 0

class MarketSnapshotV1(BaseModel):
    items: list[MarketTickerSnapshotItemV1] = Field(default_factory=list)
    generated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class MarketSnapshotAggregatorV1:
    async def build(self, symbols: list[str], service, exchanges: list[SupportedExchange]) -> MarketSnapshotV1:
        items = []
        for exchange in exchanges:
            for symbol in symbols:
                ticker = await service.ticker(exchange, symbol)
                if ticker is None:
                    continue
                if isinstance(ticker, dict):
                    price = float(ticker.get("price", 0))
                    change = float(ticker.get("change_percent", 0))
                    volume = float(ticker.get("volume", 0))
                else:
                    price = ticker.price
                    change = ticker.change_percent
                    volume = ticker.volume
                items.append(MarketTickerSnapshotItemV1(exchange=exchange, symbol=symbol, price=price, change_percent=change, volume=volume))
        return MarketSnapshotV1(items=items)
