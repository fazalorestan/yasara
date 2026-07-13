from app.platform_core.models import PlatformCoreSummaryV422

def test_v422_platform_summary():
    s=PlatformCoreSummaryV422(); assert s.ready is True; assert s.no_new_trading_features is True
