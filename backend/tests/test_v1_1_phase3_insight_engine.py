from app.v11_ai_market_intelligence.insight_engine import AIMarketInsightEngineV11
from app.v11_market_data.models import MarketSnapshotItemV11

def test_insight_engine():
    item = MarketSnapshotItemV11(exchange="binance", symbol="BTCUSDT", normalized_symbol="BTCUSDT", last_price=50000, bid=49999, ask=50001, volume_24h=10)
    insight = AIMarketInsightEngineV11().analyze_item(item)
    assert insight.ready is True
    assert insight.symbol == "BTCUSDT"
