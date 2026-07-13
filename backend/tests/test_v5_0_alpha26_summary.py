from app.v500_alpha26_portfolio_manager.models import PortfolioManagerSummaryV500Alpha26

def test_v500_alpha26_summary():
    s=PortfolioManagerSummaryV500Alpha26(); assert s.ready is True; assert s.real_execution_enabled is False
