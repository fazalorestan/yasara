from app.desktop_ui_v1.feed_aggregator import DesktopUIFeedAggregatorV1

def test_desktop_api_feed_model():
    feed = DesktopUIFeedAggregatorV1().build("light")
    assert feed.theme["mode"] == "light"
