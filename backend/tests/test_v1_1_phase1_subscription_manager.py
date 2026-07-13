from app.v11_market_data.models import SubscriptionRequestV11
from app.v11_market_data.subscriptions import SubscriptionManagerV11

def test_subscription_manager():
    manager = SubscriptionManagerV11()
    state = manager.subscribe(SubscriptionRequestV11(exchange="binance", symbols=["BTC-USDT", "ETHUSDT"]))
    assert state.exchange == "binance"
    assert "BTCUSDT" in state.symbols
