from datetime import datetime, timedelta, timezone
from app.intelligence_v1.engine.market_intelligence import MarketIntelligenceEngineV1
from app.market_data.domain.models import Candle, ExchangeCode

def candles(n=260):
    start = datetime.now(timezone.utc) - timedelta(minutes=n)
    out = []
    for i in range(n):
        price = 100 + i * 0.1
        out.append(Candle(
            exchange=ExchangeCode.BINANCE_FUTURES,
            symbol="BTC/USDT",
            timeframe="1m",
            open_time=start + timedelta(minutes=i),
            close_time=start + timedelta(minutes=i+1),
            open=price,
            high=price + 1,
            low=price - 1,
            close=price + 0.5,
            volume=100 + i,
        ))
    return out

def test_market_intelligence_report():
    report = MarketIntelligenceEngineV1().analyze("binance_futures", "BTC/USDT", {"1m": candles()})
    assert report.symbol == "BTC/USDT"
    assert report.confidence > 0
    assert "1m" in report.timeframes
