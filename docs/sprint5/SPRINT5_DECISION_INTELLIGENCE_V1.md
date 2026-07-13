# Sprint 5 — Decision Intelligence Engine v1

## Implemented
- Decision Object v1
- Confidence breakdown
- Weighted scoring
- Rule Engine
- Strategy Plugins
- Signal Plan Builder
- Explainability
- Ranking
- Live/stored Decision API
- Desktop Decision Client/Panel scaffold
- Unit tests

## API
- `GET /api/v1/decision-v1/binance_futures/live/BTC/USDT`
- `GET /api/v1/decision-v1/binance_futures/stored/BTC/USDT`
- `POST /api/v1/decision-v1/binance_futures/rank/live`

## Important
This sprint does not execute trades. It only produces explainable decisions and signal plans.
