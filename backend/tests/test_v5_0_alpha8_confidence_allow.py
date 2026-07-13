from app.platform_core.indicators.signal_logic_expansion.confidence_policy import DirectionConfidencePolicy
def test_v500_alpha8_confidence_allow():
    assert DirectionConfidencePolicy().allow_direction("LONG", 60) is True
