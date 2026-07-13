from app.desktop_ui_v1.feed_aggregator import DesktopUIFeedAggregatorV1

def test_desktop_ui_feed():
    feed = DesktopUIFeedAggregatorV1().build()
    assert "chart" in feed.widgets
    assert feed.theme["mode"] == "dark"
