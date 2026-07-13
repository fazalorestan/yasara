from app.platform_core.optimizer.scoring import OptimizerScoringService

def test_v500_alpha31_score_pnl(): assert OptimizerScoringService().score({'net_pnl':10})['score'] == 10
