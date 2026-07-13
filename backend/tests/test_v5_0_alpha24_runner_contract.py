from app.platform_core.runtime_api_smoke.runner_contract import RuntimeAPISmokeRunnerContract

def test_v500_alpha24_runner_contract():
    r=RuntimeAPISmokeRunnerContract().static_run(); assert r['ready'] is True; assert r['failed_count'] == 0
