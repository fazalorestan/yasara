from app.v45_paper_trading.service import PaperTradingExecutionServiceV45

def test_v45_mark_to_market():
    data = PaperTradingExecutionServiceV45().mark_to_market()
    assert data["ready"] is True
    assert "account" in data
