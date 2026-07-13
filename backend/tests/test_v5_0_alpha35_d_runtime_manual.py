from app.platform_core.portfolio_intelligence.enterprise.runtime_acceptance import PortfolioEnterpriseRuntimeAcceptance

def test_v500_alpha35_d_runtime_manual(): assert PortfolioEnterpriseRuntimeAcceptance().contract()['manual_apply_required'] is False