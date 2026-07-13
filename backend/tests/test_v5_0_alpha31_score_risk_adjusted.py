from app.platform_core.optimizer.scoring import OptimizerScoringService

def test_v500_alpha31_score_risk_adjusted(): assert OptimizerScoringService().score({'net_pnl':100,'max_drawdown_pct':2}, 'risk_adjusted')['score'] == 80
