from app.v11_market_data.engine import MarketDataEngineV11
from app.v11_market_data.models import SubscriptionRequestV11

def test_market_data_engine_integration():
    engine = MarketDataEngineV11()
    engine.subscribe(SubscriptionRequestV11(exchange="binance", symbols=["BTCUSDT"]))
    engine.ingest_synthetic_ticker("binance", "BTCUSDT", 50000)
    status = engine.status()
    assert status["ready"] is True
    assert status["events"] == 1
    assert status["snapshot_count"] == 1
