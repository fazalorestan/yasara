# Sprint 2 — Realtime Market Data

## Implemented
- Binance Futures WebSocket Manager
- Kline, ticker and depth subscriptions
- WebSocket reconnect and heartbeat
- Async Market Event Bus
- Binance stream normalizer
- Realtime API endpoints
- Candle sync service scaffold
- Gap detection logic
- Desktop market data client scaffold
- Tests for normalizer and event bus

## API
- `POST /api/v1/market-data/realtime/binance/start`
- `POST /api/v1/market-data/realtime/binance/stop`
- `GET /api/v1/market-data/realtime/stats`

## Next Sprint
Sprint 3 should wire database session dependency for sync persistence, add background scheduler, and connect desktop chart to real candles.
