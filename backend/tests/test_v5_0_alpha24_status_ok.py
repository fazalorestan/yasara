from app.platform_core.runtime_api_smoke.status_validator import RuntimeAPIStatusValidator

def test_v500_alpha24_status_ok(): assert RuntimeAPIStatusValidator().validate_status(200)['valid'] is True
