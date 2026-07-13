from app.v25_risk_backtest_paper.service import RiskBacktestPaperServiceV25
from app.v25_risk_backtest_paper.models import PaperOrderV25

def test_v25_paper_order():
    service = RiskBacktestPaperServiceV25()
    o = service.paper_order(PaperOrderV25())
    assert o["ready"] is True
    assert o["order"]["mode"] == "paper"
    assert service.paper_state()["orders_count"] == 1
