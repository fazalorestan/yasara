from app.platform_core.optimizer.config import OptimizerConfigService

def test_v500_alpha31_config(): assert OptimizerConfigService().default()['execution_allowed'] is False
