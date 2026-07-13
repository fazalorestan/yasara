from app.platform_core.broker.models import BrokerOrderRequest

def test_v500_alpha22_order_request():
    r=BrokerOrderRequest(symbol='BTCUSDT', side='buy', order_type='market', quantity=1); assert r.quantity == 1
