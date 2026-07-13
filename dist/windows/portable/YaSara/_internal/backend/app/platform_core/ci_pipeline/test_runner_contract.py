class AutomatedTestRunnerContract:
    def contract(self):
        return {
            "ready": True,
            "runner": "pytest_contract",
            "command": "python yasara.py test",
            "runs_all_tests": True,
            "requires_zero_failures": True,
            "writes_test_report": True,
            "real_execution_enabled": False,
        }

automated_test_runner_contract = AutomatedTestRunnerContract()
