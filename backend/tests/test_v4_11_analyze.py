from app.v411_smart_money_pro.models import SmartMoneyProRequestV411
from app.v411_smart_money_pro.service import SmartMoneyProServiceV411
def test_v411_analyze():
    data=SmartMoneyProServiceV411().analyze(SmartMoneyProRequestV411(limit=100))
    assert data["ready"] is True
    assert "smart_money_pro" in data
    assert data["real_order_execution_enabled"] is False
