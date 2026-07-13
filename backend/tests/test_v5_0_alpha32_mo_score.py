from app.platform_core.optimizer_pro.multi_objective import MultiObjectiveScoringService

def test_v500_alpha32_mo_score(): assert MultiObjectiveScoringService().score({'net_pnl':100})['ready'] is True