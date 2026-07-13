from app.platform_core.portfolio_manager.equity_curve import EquityCurveService

def test_v500_alpha26_equity_curve(): assert len(EquityCurveService().build_sample()['points'])==3
