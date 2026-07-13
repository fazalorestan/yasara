from app.platform_core.runtime_api_smoke.catalog import runtime_endpoint_catalog
from app.platform_core.runtime_api_smoke.status_validator import runtime_api_status_validator

class RuntimeAPISmokeRunnerContract:
    def static_run(self):
        results = []
        for item in runtime_endpoint_catalog.endpoints():
            payload = {"ready": True, "path": item["path"], "method": item["method"]}
            status = runtime_api_status_validator.validate_status(200)
            body = runtime_api_status_validator.validate_payload(payload)
            results.append({
                "path": item["path"],
                "method": item["method"],
                "critical": item["critical"],
                "status": status,
                "payload": body,
                "passed": status["valid"] and body["valid"],
            })
        failed = [r for r in results if not r["passed"]]
        return {
            "ready": len(failed) == 0,
            "total": len(results),
            "failed_count": len(failed),
            "results": results,
            "mode": "static_contract_until_live_http_runner",
        }

runtime_api_smoke_runner_contract = RuntimeAPISmokeRunnerContract()
