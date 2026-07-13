from app.market_tools_v1.signal_quality import SignalQualityEngineV1, SignalQualityInputV1

def test_signal_quality_grade_a():
    result = SignalQualityEngineV1().evaluate(SignalQualityInputV1(confidence=95, liquidity_score=95, volatility_percent=1))
    assert result.grade == "A"
