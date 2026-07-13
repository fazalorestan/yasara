from app.v11_paper_trading.models import PaperAccountV11
from app.v11_risk_control.daily_loss_guard import DailyLossGuardV11

def test_daily_loss_guard_blocks_large_loss():
    account = PaperAccountV11(realized_pnl=-1000)
    result = DailyLossGuardV11().check(account)
    assert result.allowed is False
