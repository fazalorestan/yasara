# Sprint 6 — Risk Intelligence Engine v1

## Implemented
- Risk profiles: Conservative, Balanced, Aggressive
- Account snapshot
- Risk limits
- Existing exposure model
- Risk/reward validation
- Risk rules engine
- Confidence-adjusted position sizing
- Risk assessment object
- Live/stored Risk API
- Desktop Risk Intelligence client scaffold
- Unit tests

## API
- `POST /api/v1/risk-v1/binance_futures/live/BTC/USDT`
- `POST /api/v1/risk-v1/binance_futures/stored/BTC/USDT`

## Important
This sprint still does not execute trades. It only validates and adjusts decisions before any future execution.
