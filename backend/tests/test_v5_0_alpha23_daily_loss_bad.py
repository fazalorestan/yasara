from app.platform_core.risk_engine.daily_loss import DailyLossGuard

def test_v500_alpha23_daily_loss_bad(): assert DailyLossGuard().check(4,3)['reason']=='max_daily_loss_exceeded'
