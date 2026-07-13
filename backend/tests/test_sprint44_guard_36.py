from app.v52_ai_decision_engine.models import DecisionResult, DecisionDirection
def test_guard():
    r=DecisionResult(symbol="X", timeframe="1h", decision=DecisionDirection.WAIT, confidence=0, quality_score=0)
    assert r.mock_data is False
