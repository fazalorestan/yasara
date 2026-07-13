class TestStateRegistry:
    def snapshot(self):
        return {
            "ready": True,
            "tests_total": 4128,
            "tests_passed": 4128,
            "tests_failed": 0,
            "tests_errors": 0,
            "last_regression_status": "pass",
            "current_package_expected_tests": 80,
        }
test_state_registry = TestStateRegistry()
