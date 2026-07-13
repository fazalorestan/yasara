from app.v45_paper_trading.models import PaperAccountResetV45, PaperOrderRequestV45
from app.v45_paper_trading.service import PaperTradingExecutionServiceV45

def test_v45_place_order():
    s = PaperTradingExecutionServiceV45()
    s.reset(PaperAccountResetV45(balance=10000))
    data = s.place_order(PaperOrderRequestV45(quantity=0.01))
    assert data["ready"] is True
    assert data["result"]["accepted"] is True
    assert data["real_order_execution_enabled"] is False
