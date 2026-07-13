from app.platform_core.api_health.catalog import api_endpoint_catalog
from app.platform_core.api_health.validators import api_response_validator

class APISmokeTestRunner:
    def run_static(self):
        results = []
        for item in api_endpoint_catalog.endpoints():
            payload = {"ready": True, "path": item["path"], "method": item["method"]}
            status = api_response_validator.validate_status(200)
            json_check = api_response_validator.validate_json(payload)
            ready_check = api_response_validator.validate_ready_field(payload)
            passed = status["valid"] and json_check["valid"] and ready_check["valid"]
            results.append({"path": item["path"], "method": item["method"], "critical": item["critical"], "status": status, "json": json_check, "ready_field": ready_check, "passed": passed})
        failed = [r for r in results if not r["passed"]]
        return {"ready": len(failed) == 0, "mode": "static_smoke_contract", "results": results, "failed_count": len(failed), "total": len(results)}

api_smoke_test_runner = APISmokeTestRunner()
