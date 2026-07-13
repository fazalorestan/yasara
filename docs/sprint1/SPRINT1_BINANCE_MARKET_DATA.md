# Sprint 1 — Binance Market Data Core

## Goal
Build the first real market data core for YaSara using Binance Futures public REST endpoints.

## Implemented
- Binance Futures Adapter
- Normalized domain models
- REST client with retry/backoff
- TTL cache
- Market data API endpoints
- PostgreSQL candle table migration
- Candle repository
- Unit tests for normalization/mapping
- Docker PostgreSQL service

## API
- `GET /api/v1/market-data/health`
- `GET /api/v1/market-data/binance_futures/symbols`
- `GET /api/v1/market-data/binance_futures/ticker/BTC/USDT`
- `GET /api/v1/market-data/binance_futures/candles/BTC/USDT?timeframe=15m&limit=200`
- `GET /api/v1/market-data/binance_futures/order-book/BTC/USDT`
- `GET /api/v1/market-data/binance_futures/funding-rate/BTC/USDT`
- `GET /api/v1/market-data/binance_futures/open-interest/BTC/USDT`

## Next Sprint
Sprint 2 should add WebSocket streams, persistence sync jobs and dashboard binding.
