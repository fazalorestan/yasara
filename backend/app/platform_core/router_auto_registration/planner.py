from app.platform_core.router_auto_registration.discovery import route_module_discovery
from app.platform_core.router_auto_registration.importer import route_module_importer

class RouterAutoRegistrationPlanner:
    def build_plan(self):
        discovered = route_module_discovery.discover()
        inspected = [route_module_importer.inspect(item["import_path"]) | item for item in discovered]
        valid = [item for item in inspected if item["ready"]]
        invalid = [item for item in inspected if not item["ready"]]
        return {
            "ready": len(invalid) == 0,
            "total_modules": len(discovered),
            "valid_routers": len(valid),
            "invalid_routers": len(invalid),
            "items": inspected,
            "mode": "auto_registration_plan",
        }

router_auto_registration_planner = RouterAutoRegistrationPlanner()
