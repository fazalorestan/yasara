from app.v412_smart_money_pro_sprint2.models import SmartMoneyProSprint2RequestV412
from app.v412_smart_money_pro_sprint2.service import SmartMoneyProSprint2ServiceV412
def test_v412_analyze():
    data=SmartMoneyProSprint2ServiceV412().analyze(SmartMoneyProSprint2RequestV412(limit=100))
    assert data["ready"] is True
    assert "smart_money_pro_sprint2" in data
    assert data["real_order_execution_enabled"] is False
