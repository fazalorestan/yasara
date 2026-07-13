from app.v32_advanced_ai_indicators.service import AdvancedAIIndicatorServiceV32

def test_v32_batch():
    data = AdvancedAIIndicatorServiceV32().batch()
    assert data["ready"] is True
    assert len(data["items"]) >= 4
