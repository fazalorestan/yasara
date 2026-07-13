from app.platform_core.api_health.service import APIHealthFrameworkService

def test_v500_alpha17_service_smoke():
    assert APIHealthFrameworkService().smoke()['ready'] is True
