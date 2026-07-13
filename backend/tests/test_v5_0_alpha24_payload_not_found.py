from app.platform_core.runtime_api_smoke.status_validator import RuntimeAPIStatusValidator

def test_v500_alpha24_payload_not_found(): assert RuntimeAPIStatusValidator().validate_payload({'detail':'Not Found'})['valid'] is False
