from app.v11_market_data.models import RateLimitRuleV11
from app.v11_market_data.rate_limit import RateLimitManagerV11

def test_rate_limit_manager():
    manager = RateLimitManagerV11()
    manager.set_rule(RateLimitRuleV11(exchange="binance", max_requests=1, per_seconds=60))
    assert manager.allow("binance") is True
    assert manager.allow("binance") is False
