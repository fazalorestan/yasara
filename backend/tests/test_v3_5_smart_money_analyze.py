from app.v35_smart_money.models import SmartMoneyRequestV35
from app.v35_smart_money.service import SmartMoneyEngineServiceV35

def test_v35_analyze():
    data = SmartMoneyEngineServiceV35().analyze(SmartMoneyRequestV35(limit=80))
    assert data["ready"] is True
    assert "smart_money" in data
    assert "score" in data
    assert data["constitution_compliant"] is True
    assert data["live_trading_enabled"] is False
