from app.platform_core.indicators.bridges.event_publisher import IndicatorEventPublisher

def test_v445_event_publisher():
    out = IndicatorEventPublisher().publish_signal({"signals": [{"direction": "WAIT", "confidence": 0}]})
    assert out["ready"] is True
    assert out["event"]["payload"]["execution_allowed"] is False
