from app.platform_core.api_routing.discovery import auto_router_discovery
from app.platform_core.api_routing.validator import router_import_validator

class RouterRegistrationPlanner:
    def build_plan(self):
        records = auto_router_discovery.discover_modules()
        validations = [router_import_validator.validate_module_record(r) for r in records]
        safe = [v for v in validations if v["valid"]]
        unsafe = [v for v in validations if not v["valid"]]
        return {
            "ready": len(unsafe) == 0,
            "total_modules": len(records),
            "safe_modules": len(safe),
            "unsafe_modules": len(unsafe),
            "items": validations,
            "mode": "registration_plan_only",
        }

router_registration_planner = RouterRegistrationPlanner()
