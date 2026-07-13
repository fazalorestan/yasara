from app.platform_core.optimizer.service import OptimizerFoundationService

def test_v500_alpha31_service_ranking(): assert OptimizerFoundationService().ranking()['ready'] is True
