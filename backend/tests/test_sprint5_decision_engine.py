from datetime import datetime, timedelta, timezone
from app.decision_v1.engine.decision_engine import DecisionEngineV1
from app.decision_v1.domain.models import DecisionDirection
from app.intelligence_v1.engine.market_intelligence import MarketIntelligenceEngineV1
from app.market_data.domain.models import Candle, ExchangeCode

def make_candles(n=260):
    start = datetime.now(timezone.utc) - timedelta(minutes=n)
    out = []
    for i in range(n):
        price = 100 + i * 0.2
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

def test_decision_engine_generates_object():
    report = MarketIntelligenceEngineV1().analyze("binance_futures", "BTC/USDT", {"1m": make_candles(), "15m": make_candles()})
    decision = DecisionEngineV1().decide(report)
    assert decision.symbol == "BTC/USDT"
    assert decision.direction in list(DecisionDirection)
    assert 0 <= decision.scores.confidence <= 100
    assert decision.explanation.summary
    assert decision.rules
    assert decision.strategies
