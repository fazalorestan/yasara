from app.v32_advanced_ai_indicators.service import AdvancedAIIndicatorServiceV32

def test_v32_summary():
    s = AdvancedAIIndicatorServiceV32().summary()
    assert s.product_progress_percent == 57
    assert s.remaining_to_professional_product_percent == 43
