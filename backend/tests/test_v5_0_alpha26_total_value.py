from app.platform_core.portfolio_manager.valuation import PortfolioValuationService

def test_v500_alpha26_total_value(): assert PortfolioValuationService().total_holdings_value([{'quantity':2,'last_price':10}])==20
