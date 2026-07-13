from app.platform_core.runtime_api_smoke.service import RuntimeAPISmokeService

def test_v500_alpha24_service_runner(): assert RuntimeAPISmokeService().runner()['ready'] is True
