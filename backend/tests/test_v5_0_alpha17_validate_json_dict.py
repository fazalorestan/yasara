from app.platform_core.api_health.validators import APIResponseValidator

def test_v500_alpha17_validate_json_dict():
    assert APIResponseValidator().validate_json({'ready': True})['valid'] is True
