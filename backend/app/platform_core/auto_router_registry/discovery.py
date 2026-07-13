import importlib
import pkgutil

class AutoRouterDiscovery:
    def discover_modules(self, package_name: str = "app.api.v1.routes") -> list[str]:
        package = importlib.import_module(package_name)
        return sorted(
            f"{package_name}.{item.name}"
            for item in pkgutil.iter_modules(package.__path__)
            if not item.name.startswith("_")
        )

    def import_module(self, module_path: str) -> dict:
        try:
            module = importlib.import_module(module_path)
            router = getattr(module, "router", None)
            return {"ready": router is not None, "module_path": module_path, "module": module, "has_router": router is not None, "error": None}
        except Exception as exc:
            return {"ready": False, "module_path": module_path, "module": None, "has_router": False, "error": str(exc)}

auto_router_discovery = AutoRouterDiscovery()
