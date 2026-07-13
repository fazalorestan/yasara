from app.v500_alpha35_portfolio_enterprise.service import PortfolioEnterpriseFacadeV500Alpha35

def test_v500_alpha35_d_contract_block(): assert PortfolioEnterpriseFacadeV500Alpha35().contract()['execution_allowed'] is False
