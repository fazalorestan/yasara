from app.platform_core.indicators.bridges.ai_bridge import IndicatorAIBridge

def test_v445_ai_bridge():
    out = IndicatorAIBridge().to_ai_decision({"signals": [{"direction": "LONG", "confidence": 70, "reason": "x"}]})
    assert out["direction"] == "LONG"
    assert out["mode"] == "analysis_only"
