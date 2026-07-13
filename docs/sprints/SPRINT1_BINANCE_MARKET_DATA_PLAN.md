# Sprint 1 — Binance Market Data Plan

## Goal
Implement real Binance public market data infrastructure.

## Scope
- Binance Futures REST adapter
- Binance WebSocket adapter
- Symbol metadata sync
- OHLCV downloader
- Ticker endpoint
- Order book snapshot endpoint
- Funding rate endpoint
- Open interest endpoint
- Normalized internal models
- PostgreSQL persistence for candles and metadata
- Integration tests with mocked HTTP/WebSocket
- Optional live smoke tests

## No API Keys Required
Sprint 1 uses public market data only.

## Deliverables
- Working `/api/v1/market/binance/symbols`
- Working `/api/v1/market/binance/ticker/{symbol}`
- Working `/api/v1/market/binance/ohlcv/{symbol}`
- Working symbol sync command
- Tests
- Documentation
