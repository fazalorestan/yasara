from app.platform_core.indicators.bridges.confidence_bridge import IndicatorConfidenceBridge

def test_v445_confidence_bridge():
    c = IndicatorConfidenceBridge()
    assert c.normalize(120) == 100
    assert c.grade(86) == "A+"
