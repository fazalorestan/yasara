from app.connectivity_v1.rate_limiter import TokenBucketRateLimiterV1

def test_rate_limiter_blocks_when_empty():
    limiter = TokenBucketRateLimiterV1(capacity=1)
    assert limiter.allow().allowed is True
    assert limiter.allow().allowed is False
    assert limiter.refill() == 1
