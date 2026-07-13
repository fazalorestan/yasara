from app.v432_platform_versioning.models import PlatformVersioningSummaryV432

def test_v432_summary():
    s = PlatformVersioningSummaryV432()
    assert s.ready is True
    assert s.no_new_trading_features is True
    assert s.live_execution_enabled is False
