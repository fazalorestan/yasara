class RegressionRunnerContract:
    def contract(self):
        return {
            "ready": True,
            "runner": "regression_contract",
            "regression_required": True,
            "backward_compatibility_required": True,
            "api_breaking_changes_allowed": False,
            "requires_zero_regression": True,
        }

regression_runner_contract = RegressionRunnerContract()
