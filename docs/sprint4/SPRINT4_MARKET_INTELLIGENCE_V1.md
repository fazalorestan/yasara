# Sprint 4 — Market Intelligence v1

## Implemented
- IndicatorCalculator: SMA, EMA, RSI, MACD, ATR, Relative Volume
- MarketStructureAnalyzer: HH/HL/LH/LL, trend, BOS
- RegimeClassifier
- IntelligenceScoringEngine
- MarketIntelligenceEngineV1
- Live and stored analysis service
- API endpoints for live/stored intelligence
- Unit tests

## API
- `GET /api/v1/intelligence-v1/binance_futures/live/BTC/USDT`
- `GET /api/v1/intelligence-v1/binance_futures/stored/BTC/USDT`

## Next Sprint
Sprint 5 should implement Decision Intelligence v1 on top of Market Intelligence v1.
