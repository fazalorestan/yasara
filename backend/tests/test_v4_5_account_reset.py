from app.v45_paper_trading.models import PaperAccountResetV45
from app.v45_paper_trading.service import PaperTradingExecutionServiceV45

def test_v45_reset_account():
    s = PaperTradingExecutionServiceV45()
    data = s.reset(PaperAccountResetV45(balance=12000))
    assert data["account"]["balance"] == 12000
