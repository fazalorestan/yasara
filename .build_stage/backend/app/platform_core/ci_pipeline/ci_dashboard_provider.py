from app.platform_core.ci_pipeline.test_result_registry import test_result_registry
from app.platform_core.ci_pipeline.coverage_contract import coverage_contract_service

class CIDashboardProvider:
    def dashboard(self):
        results = test_result_registry.results()
        coverage = coverage_contract_service.contract()
        return {
            "ready": True,
            "build_id": results["build_id"],
            "tests_total": results["tests_total"],
            "tests_passed": results["tests_passed"],
            "tests_failed": results["tests_failed"],
            "tests_errors": results["tests_errors"],
            "regression": results["regression"],
            "coverage_enabled": coverage["coverage_enabled"],
            "source": "ci_pipeline_registries",
            "hardcoded_dashboard": False,
        }

ci_dashboard_provider = CIDashboardProvider()
