from app.platform_core.ci_pipeline.coverage_contract import coverage_contract_service
from app.platform_core.ci_pipeline.regression_runner import regression_runner_contract
from app.platform_core.ci_pipeline.test_result_registry import test_result_registry
from app.platform_core.ci_pipeline.test_runner_contract import automated_test_runner_contract

class CITestReportService:
    def report(self):
        return {
            "ready": True,
            "test_runner": automated_test_runner_contract.contract(),
            "regression_runner": regression_runner_contract.contract(),
            "coverage": coverage_contract_service.contract(),
            "results": test_result_registry.results(),
            "zero_failures_required": True,
            "backward_compatibility_required": True,
            "real_execution_enabled": False,
            "real_broker_connection_enabled": False,
        }

ci_test_report_service = CITestReportService()
CITestReport = CITestReportService
ci_test_report = ci_test_report_service
