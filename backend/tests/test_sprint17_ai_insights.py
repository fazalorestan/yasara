import pytest
from app.production_ai_v1.application.service import ProductionAIServiceV1

@pytest.mark.asyncio
async def test_ai_signal_explanation():
    insight = await ProductionAIServiceV1().explain_signal("BTC/USDT", "long", 82, ["Trend bullish", "Volume rising"])
    assert insight.confidence == 82
    assert "Trend bullish" in insight.explanation
