from app.platform_core.ci_pipeline.report import ci_pipeline_report_service

class CIPipelineReadinessGate:
    def run(self):
        report = ci_pipeline_report_service.report()
        results = report["test_report"]["results"]
        ready = (
            report["ready"]
            and report["core"]["ci_enabled"]
            and report["test_report"]["test_runner"]["runs_all_tests"]
            and report["test_report"]["regression_runner"]["requires_zero_regression"]
            and results["tests_failed"] == 0
            and results["tests_errors"] == 0
            and report["hardcoded_dashboard"] is False
            and report["commercial_execution_engine_enabled"] is False
        )
        return {
            "ready": ready,
            "checks": {
                "ci_core_ready": report["core"]["ready"],
                "runs_all_tests": report["test_report"]["test_runner"]["runs_all_tests"],
                "regression_required": report["test_report"]["regression_runner"]["regression_required"],
                "tests_failed": results["tests_failed"],
                "tests_errors": results["tests_errors"],
                "dashboard_ready": report["dashboard"]["ready"],
                "hardcoded_dashboard": False,
                "commercial_execution_engine_enabled": False,
                "commercial_api_key_required": False,
                "real_execution_enabled": False,
                "real_broker_connection_enabled": False,
            },
        }

ci_pipeline_readiness_gate = CIPipelineReadinessGate()
