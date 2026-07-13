from app.v32_advanced_ai_indicators.service import AdvancedAIIndicatorServiceV32
from app.v32_advanced_ai_indicators.models import AdvancedIndicatorRequestV32

def test_v32_analyze():
    data = AdvancedAIIndicatorServiceV32().analyze(AdvancedIndicatorRequestV32(limit=80))
    assert data["ready"] is True
    assert "indicators" in data
    assert data["ai_signal"]["direction"] in ["long", "short", "wait"]
    assert data["live_trading_enabled"] is False
