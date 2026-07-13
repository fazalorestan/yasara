from app.v500_alpha26_portfolio_manager.service import PortfolioManagerFacadeV500Alpha26

def test_v500_alpha26_facade_summary(): assert PortfolioManagerFacadeV500Alpha26().summary().ready is True
