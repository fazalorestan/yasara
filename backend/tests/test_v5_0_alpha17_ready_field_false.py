from app.platform_core.api_health.validators import APIResponseValidator

def test_v500_alpha17_ready_field_false():
    assert APIResponseValidator().validate_ready_field({'ready': False})['valid'] is False
