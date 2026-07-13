from app.platform_core.build_pipeline.validators import BuildValidatorService

def test_validation(): assert BuildValidatorService().validate()['build_valid'] is True
