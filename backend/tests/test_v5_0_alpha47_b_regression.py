from app.platform_core.ci_pipeline.regression_runner import RegressionRunnerContract

def test_regression(): assert RegressionRunnerContract().contract()['requires_zero_regression'] is True
