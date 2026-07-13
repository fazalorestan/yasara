from app.platform_core.ci_pipeline.test_result_registry import test_result_registry

class CISignalProvider:
    def signal(self):
        results = test_result_registry.results()
        return {
            "ready": True,
            "tests_total": results["tests_total"],
            "tests_passed": results["tests_passed"],
            "tests_failed": results["tests_failed"],
            "tests_errors": results["tests_errors"],
            "regression": results["regression"],
            "signal": "green" if results["tests_failed"] == 0 and results["tests_errors"] == 0 else "red",
            "hardcoded_dashboard": False,
        }

ci_signal_provider = CISignalProvider()
