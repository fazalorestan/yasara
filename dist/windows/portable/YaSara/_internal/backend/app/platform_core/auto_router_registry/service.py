from app.platform_core.auto_router_registry.discovery import auto_router_discovery

class AutoRouterRegistryService:
    def discover(self):
        modules = auto_router_discovery.discover_modules()
        return {"ready": True, "modules": modules, "count": len(modules)}

    def contract(self):
        return {"ready": True, "strategy": "startup_auto_discovery", "manual_router_patch_required_after_this": False, "duplicate_route_protection": True, "invalid_module_isolated": True, "real_execution_enabled": False, "auto_trading_enabled": False}

auto_router_registry_service = AutoRouterRegistryService()
