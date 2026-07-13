from app.platform_core.ci_pipeline.test_result_registry import test_result_registry

class CIPanelContract:
    def panel(self):
        results = test_result_registry.results()
        return {
            "ready": True,
            "panel": "ci",
            "tests_total": results["tests_total"],
            "tests_passed": results["tests_passed"],
            "tests_failed": results["tests_failed"],
            "regression": results["regression"],
        }

ci_panel_contract = CIPanelContract()
