from app.platform_core.api_health.validators import APIResponseValidator

def test_v500_alpha17_validate_status_ok():
    assert APIResponseValidator().validate_status(200)['valid'] is True
