from app.platform_core.optimizer_pro.multi_objective import MultiObjectiveScoringService

def test_v500_alpha32_mo_components(): assert 'components' in MultiObjectiveScoringService().score({'net_pnl':1})