from app.platform_core.optimizer.scoring import OptimizerScoringService

def test_v500_alpha31_score_bad(): assert OptimizerScoringService().score({}, 'bad')['ready'] is False
