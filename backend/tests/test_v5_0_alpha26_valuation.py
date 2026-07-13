from app.platform_core.portfolio_manager.valuation import PortfolioValuationService

def test_v500_alpha26_valuation(): assert PortfolioValuationService().holding_value(2,10)==20
