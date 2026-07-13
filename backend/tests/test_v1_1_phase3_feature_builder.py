from app.v11_ai_market_intelligence.feature_builder import MarketFeatureBuilderV11
from app.v11_market_data.models import MarketSnapshotItemV11

def test_feature_builder():
    item = MarketSnapshotItemV11(exchange="binance", symbol="BTCUSDT", normalized_symbol="BTCUSDT", last_price=50000, bid=49999, ask=50001, volume_24h=10)
    features = MarketFeatureBuilderV11().from_snapshot_item(item)
    assert features.symbol == "BTCUSDT"
    assert features.momentum_score > 0
