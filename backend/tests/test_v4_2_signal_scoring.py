from app.v42_signal_engine.scoring import SignalScoringEngineV42

def test_v42_scoring():
    s = SignalScoringEngineV42()
    result = s.merge([
        {"bias": "bullish", "confidence": 80, "weight": 1, "reasons": ["a"]},
        {"bias": "bullish", "confidence": 70, "weight": 1, "reasons": ["b"]},
    ])
    assert result["direction"] == "bullish"
    assert result["action"] in ["long", "short", "wait"]
