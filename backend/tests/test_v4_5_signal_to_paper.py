from app.v45_paper_trading.models import SignalPaperRequestV45
from app.v45_paper_trading.service import PaperTradingExecutionServiceV45

def test_v45_signal_to_paper():
    data = PaperTradingExecutionServiceV45().signal_to_paper(SignalPaperRequestV45())
    assert data["ready"] is True
    assert data["real_order_execution_enabled"] is False
