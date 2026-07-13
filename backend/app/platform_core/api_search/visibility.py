from app.platform_core.api_search.swagger_sync import swagger_sync_contract

class RuntimeAPIVisibilityReport:
    def report(self, runtime_paths: list[str] | None = None):
        expected = swagger_sync_contract.expected()["expected_paths"]
        available = set(expected if runtime_paths is None else runtime_paths)
        missing = [path for path in expected if path not in available]
        return {"ready": len(missing) == 0, "expected_count": len(expected), "available_count": len(available), "missing": missing, "execution_allowed": False}

runtime_api_visibility_report = RuntimeAPIVisibilityReport()
