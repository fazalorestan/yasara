from app.platform_core.runtime_api_smoke.status_validator import RuntimeAPIStatusValidator

def test_v500_alpha24_payload_ok(): assert RuntimeAPIStatusValidator().validate_payload({'ready': True})['valid'] is True
