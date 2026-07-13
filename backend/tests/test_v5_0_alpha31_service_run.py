from app.platform_core.optimizer.service import OptimizerFoundationService

def test_v500_alpha31_service_run(): assert OptimizerFoundationService().run()['execution_allowed'] is False
