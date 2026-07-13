from app.platform_core.indicators.alerts.deduplication import IndicatorAlertDeduplicator

def test_v447_deduplication():
    d = IndicatorAlertDeduplicator()
    assert d.should_emit("BTC", "LONG", 88) is True
    assert d.should_emit("BTC", "LONG", 88) is False
