from app.ai_trading_v1.confidence_engine import ConfidenceEngineV1, ConfidenceFactorsV1

def test_confidence_engine_bounds():
    score = ConfidenceEngineV1().calculate(ConfidenceFactorsV1(signal_quality=100, liquidity_score=100, data_quality=100, risk_penalty=0))
    assert score <= 100
    assert score > 80
