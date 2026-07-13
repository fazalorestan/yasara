from app.market_tools_v1.dashboard_feed import DashboardFeedBuilderV1

def test_dashboard_feed_basic():
    feed = DashboardFeedBuilderV1().build_basic(total_symbols=3, active_exchanges=2, alerts_triggered=1)
    assert len(feed.items) == 3
    assert feed.items[-1].severity == "warning"
