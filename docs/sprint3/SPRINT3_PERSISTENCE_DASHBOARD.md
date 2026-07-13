# Sprint 3 — Persistence + Dashboard Binding

## Implemented
- AsyncSession DI usage in market sync endpoints
- PostgreSQL candle persistence endpoint
- Stored candle read endpoint
- Gap detection endpoint
- Latest gap repair endpoint
- Background scheduler scaffold using APScheduler
- Desktop MarketDataClient updated for live/stored candles
- RealMarketPage scaffold for live Binance candles
- Tests for scheduler and timeframe/gap utilities

## New API
- `POST /api/v1/market-data/{exchange}/sync-candles-db/{symbol}`
- `GET /api/v1/market-data/{exchange}/stored-candles/{symbol}`
- `GET /api/v1/market-data/{exchange}/gaps/{symbol}`
- `POST /api/v1/market-data/{exchange}/repair-gap/{symbol}`
- `POST /api/v1/market-data/scheduler/jobs`
- `GET /api/v1/market-data/scheduler/stats`

## Next Sprint
Sprint 4 should implement Market Intelligence v1 on top of real persisted candles.
