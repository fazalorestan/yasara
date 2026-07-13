from app.platform_core.api_health.runner import APISmokeTestRunner

def test_v500_alpha17_runner():
    r = APISmokeTestRunner().run_static()
    assert r['ready'] is True
    assert r['failed_count'] == 0
