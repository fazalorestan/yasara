from app.v11_exchange_connectivity.rate_profiles import ExchangeRateLimitProfileBuilderV11

def test_rate_profiles():
    profiles = ExchangeRateLimitProfileBuilderV11().build()
    assert len(profiles) == 3
    assert any(p.exchange == "binance" and p.max_requests >= 1000 for p in profiles)
