from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.market_data.domain.models import Candle, ExchangeCode
from app.market_data.infrastructure.db_models import MarketCandleORM

class CandleRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def upsert_many(self, candles: list[Candle]) -> int:
        count = 0
        for candle in candles:
            timeframe = str(candle.timeframe.value if hasattr(candle.timeframe, "value") else candle.timeframe)
            existing = await self.session.scalar(
                select(MarketCandleORM).where(
                    MarketCandleORM.exchange == candle.exchange.value,
                    MarketCandleORM.symbol == candle.symbol,
                    MarketCandleORM.timeframe == timeframe,
                    MarketCandleORM.open_time == candle.open_time,
                )
            )
            if existing:
                existing.close_time = candle.close_time
                existing.open = candle.open
                existing.high = candle.high
                existing.low = candle.low
                existing.close = candle.close
                existing.volume = candle.volume
                existing.quote_volume = candle.quote_volume
                existing.trades = candle.trades
            else:
                self.session.add(MarketCandleORM(
                    exchange=candle.exchange.value,
                    symbol=candle.symbol,
                    timeframe=timeframe,
                    open_time=candle.open_time,
                    close_time=candle.close_time,
                    open=candle.open,
                    high=candle.high,
                    low=candle.low,
                    close=candle.close,
                    volume=candle.volume,
                    quote_volume=candle.quote_volume,
                    trades=candle.trades,
                ))
            count += 1
        await self.session.commit()
        return count

    async def latest(self, exchange: str, symbol: str, timeframe: str, limit: int = 500) -> list[MarketCandleORM]:
        rows = await self.session.scalars(
            select(MarketCandleORM)
            .where(
                MarketCandleORM.exchange == exchange,
                MarketCandleORM.symbol == symbol,
                MarketCandleORM.timeframe == timeframe,
            )
            .order_by(MarketCandleORM.open_time.desc())
            .limit(limit)
        )
        return list(rows)

    async def latest_as_domain(self, exchange: str, symbol: str, timeframe: str, limit: int = 500) -> list[Candle]:
        rows = await self.latest(exchange, symbol, timeframe, limit)
        rows = sorted(rows, key=lambda x: x.open_time)
        return [
            Candle(
                exchange=ExchangeCode(row.exchange),
                symbol=row.symbol,
                timeframe=row.timeframe,
                open_time=row.open_time,
                close_time=row.close_time,
                open=row.open,
                high=row.high,
                low=row.low,
                close=row.close,
                volume=row.volume,
                quote_volume=row.quote_volume,
                trades=row.trades,
                is_closed=True,
            )
            for row in rows
        ]

    async def count(self, exchange: str, symbol: str, timeframe: str) -> int:
        from sqlalchemy import func
        value = await self.session.scalar(
            select(func.count(MarketCandleORM.id)).where(
                MarketCandleORM.exchange == exchange,
                MarketCandleORM.symbol == symbol,
                MarketCandleORM.timeframe == timeframe,
            )
        )
        return int(value or 0)
