from app.platform_core.auto_router_registry.dedup import auto_router_dedup_service
from app.platform_core.auto_router_registry.discovery import auto_router_discovery

class AutoRouterRegistry:
    def register_all(self, api_router, package_name: str = "app.api.v1.routes") -> dict:
        modules = auto_router_discovery.discover_modules(package_name)
        registered, skipped, failed = [], [], []
        for module_path in modules:
            imported = auto_router_discovery.import_module(module_path)
            if not imported["ready"]:
                failed.append({"module_path": module_path, "error": imported.get("error")})
                continue
            router = getattr(imported["module"], "router", None)
            if router is None:
                skipped.append({"module_path": module_path, "reason": "no_router"})
                continue
            if auto_router_dedup_service.should_include(api_router, router):
                api_router.include_router(router)
                registered.append({"module_path": module_path, "reason": "included"})
            else:
                skipped.append({"module_path": module_path, "reason": "duplicate_or_empty"})
        return {"ready": True, "discovered": len(modules), "registered": registered, "skipped": skipped, "failed": failed, "registered_count": len(registered), "skipped_count": len(skipped), "failed_count": len(failed)}

auto_router_registry = AutoRouterRegistry()
