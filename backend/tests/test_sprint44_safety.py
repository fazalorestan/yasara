from app.v52_ai_decision_engine.models import DecisionResult, DecisionDirection
def test_safety():
    r=DecisionResult(symbol="X", timeframe="1h", decision=DecisionDirection.WAIT, confidence=0, quality_score=0)
    assert r.signal_only_default and not r.auto_trading_enabled
