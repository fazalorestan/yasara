from app.platform_core.ci_pipeline.test_runner_contract import AutomatedTestRunnerContract

def test_test_runner(): assert AutomatedTestRunnerContract().contract()['runs_all_tests'] is True
