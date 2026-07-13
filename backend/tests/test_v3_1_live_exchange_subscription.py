from app.v31_live_exchange.service import LiveExchangeServiceV31
from app.v31_live_exchange.models import LiveSubscriptionV31

def test_v31_subscription():
    service = LiveExchangeServiceV31()
    sub = service.subscribe(LiveSubscriptionV31())
    assert sub["subscribed"] is True
    assert service.realtime_status()["subscriptions_count"] == 1
