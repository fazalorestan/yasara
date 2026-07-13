from app.platform_core.indicators.signal_logic_expansion.confidence_policy import DirectionConfidencePolicy
def test_v500_alpha8_confidence_reject():
    p = DirectionConfidencePolicy()
    assert p.allow_direction("LONG", 40) is False
    assert p.normalize_direction("LONG", 40) == "WAIT"
