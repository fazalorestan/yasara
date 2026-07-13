from app.platform_core.risk_engine.daily_loss import DailyLossGuard

def test_v500_alpha23_daily_loss(): assert DailyLossGuard().check(1,3)['allowed'] is True
