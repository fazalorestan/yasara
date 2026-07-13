from app.platform_core.runtime_api_smoke.status_validator import RuntimeAPIStatusValidator

def test_v500_alpha24_status_bad(): assert RuntimeAPIStatusValidator().validate_status(404)['valid'] is False
