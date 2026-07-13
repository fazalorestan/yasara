# Sprint 7 — Backtesting Studio v1

## Implemented
- Candle Replay Engine
- Simple Breakout Strategy Backtest
- Commission, Slippage, Funding simulation
- Trade model
- Equity curve
- Drawdown
- Metrics: win rate, profit factor, expectancy, max drawdown, recovery factor, Sharpe proxy
- Monte Carlo scaffold
- Walk Forward scaffold
- Live/stored Backtest API
- Desktop Backtest client scaffold
- Unit tests

## API
- `POST /api/v1/backtest-v1/binance_futures/live`
- `POST /api/v1/backtest-v1/binance_futures/stored`
- `POST /api/v1/backtest-v1/binance_futures/monte-carlo/live`
- `POST /api/v1/backtest-v1/binance_futures/walk-forward/live`

## Next Sprint
Sprint 8 should implement Portfolio Intelligence v1.
