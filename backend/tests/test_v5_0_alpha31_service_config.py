from app.platform_core.optimizer.service import OptimizerFoundationService

def test_v500_alpha31_service_config(): assert OptimizerFoundationService().config()['ready'] is True
