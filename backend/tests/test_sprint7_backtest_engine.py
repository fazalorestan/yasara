from datetime import datetime, timedelta, timezone
from app.backtest_v1.domain.models import BacktestConfig
from app.backtest_v1.engine.backtest_engine import BacktestEngineV1
from app.market_data.domain.models import Candle, ExchangeCode

def candles(n=300):
    start = datetime.now(timezone.utc) - timedelta(minutes=n)
    out = []
    for i in range(n):
        price = 100 + i * 0.08 + (i % 7) * 0.03
        out.append(Candle(
            exchange=ExchangeCode.BINANCE_FUTURES,
            symbol="BTC/USDT",
            timeframe="15m",
            open_time=start + timedelta(minutes=15*i),
            close_time=start + timedelta(minutes=15*(i+1)),
            open=price,
            high=price + 1,
            low=price - 1,
            close=price + 0.5,
            volume=100,
        ))
    return out

def test_backtest_generates_report():
    config = BacktestConfig(symbol="BTC/USDT", timeframe="15m", initial_capital=10000)
    report = BacktestEngineV1().run(config, candles())
    assert report.config.symbol == "BTC/USDT"
    assert report.metrics.total_trades >= 0
    assert report.equity_curve
