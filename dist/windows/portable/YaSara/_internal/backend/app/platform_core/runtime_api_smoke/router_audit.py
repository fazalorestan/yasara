from app.platform_core.runtime_api_smoke.catalog import runtime_endpoint_catalog

class RouterRegistrationAudit:
    def audit(self, registered_paths: list[str] | None = None):
        expected = [item["path"] for item in runtime_endpoint_catalog.endpoints()]
        available = set(expected if registered_paths is None else registered_paths)
        missing = [path for path in expected if path not in available]
        return {
            "ready": len(missing) == 0,
            "expected_count": len(expected),
            "available_count": len(available),
            "missing": missing,
        }

router_registration_audit = RouterRegistrationAudit()
