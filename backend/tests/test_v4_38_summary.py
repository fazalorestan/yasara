from app.v438_enterprise_cache.models import EnterpriseCacheSummaryV438

def test_v438_summary():
    s = EnterpriseCacheSummaryV438()
    assert s.ready is True
    assert s.no_new_trading_features is True
    assert s.live_execution_enabled is False
