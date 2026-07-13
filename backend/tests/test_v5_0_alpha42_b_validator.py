from app.platform_core.execution_engine.order_validator import OrderValidatorService

def test_v500_alpha42_b_validator(): assert OrderValidatorService().validate()['valid'] is True
