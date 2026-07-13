from datetime import datetime, timedelta, timezone
from sqlalchemy.ext.asyncio import AsyncSession
from app.market_data.application.service import market_data_service
from app.market_data.domain.models import ExchangeCode
from app.market_data.infrastructure.repository import CandleRepository

TIMEFRAME_SECONDS = {
    "1m": 60, "3m": 180, "5m": 300, "15m": 900, "30m": 1800,
    "1h": 3600, "2h": 7200, "4h": 14400, "6h": 21600, "8h": 28800,
    "12h": 43200, "1d": 86400, "1w": 604800,
}

class MarketDataSyncService:
    async def sync_candles(
        self,
        session: AsyncSession,
        symbol: str,
        timeframe: str = "15m",
        limit: int = 500,
        exchange: ExchangeCode = ExchangeCode.BINANCE_FUTURES,
    ) -> dict:
        candles = await market_data_service.candles(symbol, timeframe, limit, exchange)
        count = await CandleRepository(session).upsert_many(candles)
        return {"symbol": symbol, "timeframe": timeframe, "exchange": exchange.value, "received": len(candles), "stored": count}

    async def stored_candles(
        self,
        session: AsyncSession,
        symbol: str,
        timeframe: str = "15m",
        limit: int = 500,
        exchange: ExchangeCode = ExchangeCode.BINANCE_FUTURES,
    ):
        return await CandleRepository(session).latest_as_domain(exchange.value, symbol, timeframe, limit)

    async def detect_gaps(
        self,
        session: AsyncSession,
        symbol: str,
        timeframe: str = "15m",
        exchange: ExchangeCode = ExchangeCode.BINANCE_FUTURES,
        limit: int = 1000,
    ) -> list[dict]:
        rows = await CandleRepository(session).latest(exchange.value, symbol, timeframe, limit)
        rows = sorted(rows, key=lambda x: x.open_time)
        expected = TIMEFRAME_SECONDS.get(timeframe, 60)
        gaps = []
        for a, b in zip(rows[:-1], rows[1:]):
            delta = (b.open_time - a.open_time).total_seconds()
            if delta > expected * 1.5:
                gaps.append({
                    "from": a.open_time.isoformat(),
                    "to": b.open_time.isoformat(),
                    "missing_seconds": delta - expected,
                    "expected_interval_seconds": expected,
                })
        return gaps

    async def repair_latest_gap(
        self,
        session: AsyncSession,
        symbol: str,
        timeframe: str = "15m",
        exchange: ExchangeCode = ExchangeCode.BINANCE_FUTURES,
    ) -> dict:
        gaps = await self.detect_gaps(session, symbol, timeframe, exchange)
        if not gaps:
            return {"repaired": False, "reason": "no_gaps"}
        gap = gaps[-1]
        start = datetime.fromisoformat(gap["from"])
        candles = await market_data_service.adapter(exchange).candles(symbol, timeframe, limit=1500, start_time=start)
        stored = await CandleRepository(session).upsert_many(candles)
        return {"repaired": True, "gap": gap, "received": len(candles), "stored": stored}

market_data_sync_service = MarketDataSyncService()
